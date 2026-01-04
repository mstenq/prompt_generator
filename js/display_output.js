import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

const NODE_NAMES = [
    "outfit-generator",
    "prompt-generator",
    "scene-generator",
    "female-generator",
    "simple-female-generator",
];

// Display text output on prompt_generator nodes
app.registerExtension({
    name: "prompt_generator.display",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        console.log("Checking node:", nodeData.name);
        // Handle both outfit-generator and prompt-generator nodes
        if (NODE_NAMES.includes(nodeData.name)) {
            console.log("Registering display extension for:", nodeData.name);
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                console.log(
                    "onExecuted called for",
                    nodeData.name,
                    "with message:",
                    message
                );
                onExecuted?.apply(this, arguments);

                if (message.text) {
                    console.log("Displaying text:", message.text);
                    // Remove existing display widgets
                    if (this.widgets) {
                        const textWidgets = this.widgets.filter(
                            (w) => w.name === "text_display"
                        );
                        textWidgets.forEach((w) => {
                            w.onRemove?.();
                            this.widgets.splice(this.widgets.indexOf(w), 1);
                        });
                    }

                    // Add new text widget with the output
                    const text = message.text[0];
                    const widget = ComfyWidgets["STRING"](
                        this,
                        "text_display",
                        ["STRING", { multiline: true }],
                        app
                    ).widget;
                    widget.inputEl.readOnly = true;
                    widget.inputEl.style.opacity = 0.6;
                    widget.value = text;

                    // Resize node to fit content
                    requestAnimationFrame(() => {
                        const sz = this.computeSize();
                        if (sz[0] < this.size[0]) sz[0] = this.size[0];
                        if (sz[1] < this.size[1]) sz[1] = this.size[1];
                        this.onResize?.(sz);
                        app.graph.setDirtyCanvas(true, false);
                    });
                } else {
                    console.log("No text in message for", nodeData.name);
                }
            };
        }
    },
});
