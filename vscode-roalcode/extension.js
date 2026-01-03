const vscode = require('vscode');
const { exec } = require('child_process');

function activate(context) {
    console.log('RoalCode extension activated');

    // --- Autocompletion ---
    const keywords = [
        "int","float","string","bool","void","map",
        "if","else","for","each","in","while","return",
        "import","from","try","catch","finally","break","continue","new",
        "public","private","protected",
        "console.print","console.scan",
        "true","false"
    ];

    const provider = vscode.languages.registerCompletionItemProvider(
        'roalcode',
        {
            provideCompletionItems(document, position) {
                const completionItems = keywords.map(kw => {
                    const item = new vscode.CompletionItem(kw, vscode.CompletionItemKind.Keyword);
                    return item;
                });
                return completionItems;
            }
        },
        '.' // déclenche autocompletion après le point
    );

    context.subscriptions.push(provider);

    // --- Commande Run RoalCode ---
    let disposable = vscode.commands.registerCommand('roalcode.run', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const code = editor.document.getText();
        const tempFile = require('path').join(require('os').tmpdir(), 'temp.rc');
        const fs = require('fs');
        fs.writeFileSync(tempFile, code);

        exec(`python main.py "${tempFile}"`, (err, stdout, stderr) => {
            if (err) vscode.window.showErrorMessage(err.message);
            vscode.window.showInformationMessage(stdout || stderr);
        });
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
