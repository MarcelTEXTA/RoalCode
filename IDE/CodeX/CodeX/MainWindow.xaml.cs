using ICSharpCode.AvalonEdit;
using ICSharpCode.AvalonEdit.Highlighting;
using ICSharpCode.AvalonEdit.Highlighting.Xshd;

using System;
using System.Diagnostics;
using System.IO;
using System.Windows;
using System.Xml;

namespace CodeX
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            LoadSyntaxHighlighting();
        }

        // 🔹 Chargement de la coloration syntaxique RoalCode
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
                    "Erreur lors du chargement de la coloration syntaxique :\n" + ex.Message,
                    "RoalCode IDE",
                    MessageBoxButton.OK,
                    MessageBoxImage.Warning
                );
            }
        }

        // ▶ Bouton Run
        private void RunButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string code = CodeEditor.Text;

                string tempFile = Path.Combine(Path.GetTempPath(), "temp.rc");
                File.WriteAllText(tempFile, code);

                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = "python", // ou "roalcode.exe" plus tard
                    Arguments = $"main.py \"{tempFile}\"",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (Process proc = new Process { StartInfo = psi })
                {
                    proc.Start();

                    string output = proc.StandardOutput.ReadToEnd();
                    string error = proc.StandardError.ReadToEnd();

                    proc.WaitForExit();

                    ConsoleOutput.Text = output + error;
                }
            }
            catch (Exception ex)
            {
                ConsoleOutput.Text = "Erreur IDE :\n" + ex.Message;
            }
        }
    }
}
