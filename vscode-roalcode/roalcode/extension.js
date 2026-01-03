const vscode = require("vscode");

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

    const keywords = [
        "int", "float", "string", "bool", "void", "map",
        "if", "else", "for", "each", "in", "while", "return",
        "import", "from", "try", "catch", "finally",
        "break", "continue", "new",
        "public", "private", "protected",
        "console.print", "console.scan",
        "true", "false"
    ];

    const provider = vscode.languages.registerCompletionItemProvider(
        "roalcode",
        {
            provideCompletionItems() {
                return keywords.map(word => {
                    const item = new vscode.CompletionItem(
                        word,
                        vscode.CompletionItemKind.Keyword
                    );
                    return item;
                });
            }
        },
        ".", // déclenche après "."
        "i", "f", "c", "p", "t" // déclencheurs
    );

    context.subscriptions.push(provider);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
