using ICSharpCode.AvalonEdit;
using ICSharpCode.AvalonEdit.CodeCompletion;
using ICSharpCode.AvalonEdit.Document;
using ICSharpCode.AvalonEdit.Editing;
using ICSharpCode.AvalonEdit.Highlighting;
using ICSharpCode.AvalonEdit.Highlighting.Xshd;

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Windows;
using System.Windows.Input;
using System.Xml;

namespace CodeX
{
    public partial class MainWindow : Window
    {
        private CompletionWindow completionWindow;

        private readonly List<string> keywords = new List<string>
        {
            "int","float","string","bool","void","map",
            "if","else","for","each","in","while","return",
            "import","from","try","catch","finally","break","continue","new",
            "public","private","protected",
            "console.print","console.scan",
            "true","false"
        };

        public MainWindow()
        {
            InitializeComponent();

            LoadSyntaxHighlighting();

            // Activation de l’autocomplétion
            CodeEditor.TextArea.TextEntered += TextEditor_TextEntered;
        }

        // ===============================
        // AUTOCOMPLÉTION
        // ===============================
        private void TextEditor_TextEntered(object sender, TextCompositionEventArgs e)
        {
            if (!char.IsLetterOrDigit(e.Text[0]) && e.Text[0] != '.')
                return;

            completionWindow = new CompletionWindow(CodeEditor.TextArea);

            IList<ICompletionData> data =
                completionWindow.CompletionList.CompletionData;

            foreach (string word in keywords)
            {
                data.Add(new MyCompletionData(word));
            }

            completionWindow.Show();
            completionWindow.Closed += (o, args) => completionWindow = null;
        }

        // ===============================
        // COLORATION SYNTAXIQUE
        // ===============================
        private void LoadSyntaxHighlighting()
        {
            try
            {
                using (var stream = File.OpenRead("RoalCode.xshd"))
                using (var reader = new XmlTextReader(stream))
                {
                    CodeEditor.SyntaxHighlighting =
                        HighlightingLoader.Load(reader, HighlightingManager.Instance);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    "Erreur coloration syntaxique :\n" + ex.Message,
                    "RoalCode IDE",
                    MessageBoxButton.OK,
                    MessageBoxImage.Warning
                );
            }
        }

        // ===============================
        // BOUTON RUN
        // ===============================
        private void RunButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string code = CodeEditor.Text;
                string tempFile = Path.Combine(Path.GetTempPath(), "temp.rc");

                File.WriteAllText(tempFile, code);

                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = $"main.py \"{tempFile}\"",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (Process proc = new Process { StartInfo = psi })
                {
                    proc.Start();
                    ConsoleOutput.Text =
                        proc.StandardOutput.ReadToEnd() +
                        proc.StandardError.ReadToEnd();
                    proc.WaitForExit();
                }
            }
            catch (Exception ex)
            {
                ConsoleOutput.Text = "Erreur IDE :\n" + ex.Message;
            }
        }
    }

    // ===============================
    // DONNÉES D’AUTOCOMPLÉTION
    // ===============================
    public class MyCompletionData : ICompletionData
    {
        public MyCompletionData(string text)
        {
            Text = text;
        }

        public System.Windows.Media.ImageSource Image => null;
        public string Text { get; }
        public object Content => Text;
        public object Description => $"Mot-clé ou fonction RoalCode : {Text}";
        public double Priority => 0;

        public void Complete(
            TextArea textArea,
            ISegment completionSegment,
            EventArgs insertionRequestEventArgs)
        {
            textArea.Document.Replace(completionSegment, Text);
        }
    }
}
