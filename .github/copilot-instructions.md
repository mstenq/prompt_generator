# ComfyUI Outfit Generator - Copilot Instructions

## Project Architecture

This is a **ComfyUI custom node** that generates random outfit descriptions for AI image prompts. Built on Vue.js frontend with ComfyUI backend integration, it combines clothing items with random colors/styles to create prompt-ready text strings.

### Key Components

- **Python Backend**: `ComfyUIFEExampleVueBasic.py` - Defines the ComfyUI node and outfit generation logic
- **Frontend Entry**: `src/main.ts` - Registers the Vue component as a ComfyUI extension
- **Vue Components**: `src/components/` - UI for outfit configuration and generation controls
- **Build Output**: `js/` directory - Vite builds frontend assets here for ComfyUI consumption

### Core Functionality

**Outfit Generation**:
- Combines clothing types (tops, bottoms, accessories) with random attributes
- Generates color palettes and style combinations
- Outputs formatted strings ready for AI image prompts
- Example output: "casual blue jeans, red cotton t-shirt, white sneakers, denim jacket"

### Critical Integration Patterns

**ComfyUI Extension Registration** (src/main.ts):
```typescript
comfyApp.registerExtension({
    name: 'vue-basic',
    getCustomWidgets(app) {
        return {
            CUSTOM_VUE_COMPONENT_BASIC(node) {
                const widget = new ComponentWidgetImpl({
                    node, name: inputSpec.name, component: VueExampleComponent
                })
                addWidget(node, widget)
                return {widget}
            }
        }
    }
})
```

**Data Serialization** (VueExampleComponent.vue):
- Vue components communicate with ComfyUI via `widget.serializeValue`
- Outfit data is serialized as text strings for prompt generation
- Returns outfit description strings ready for AI image generation

### Development Workflow

**Build Process**:
```bash
bun install    # Install Vue/Vite dependencies
bun run build  # Builds to js/ directory (consumed by ComfyUI)
```

**File Structure Logic**:
- `__init__.py` registers the Python node class and sets `EXTENSION_WEB_DIRS`
- `pyproject.toml` defines the project metadata for ComfyUI Manager
- Vite config externalizes ComfyUI scripts and Vue dependencies (assumes they're globally available)

### ComfyUI-Specific Conventions

**Node Definition Pattern**:
- INPUT_TYPES must match the widget type key (e.g., "CUSTOM_VUE_COMPONENT_BASIC")
- Node returns tuples matching RETURN_TYPES
- Category "examples" places node in ComfyUI's examples section

**Frontend Dependencies**:
- Vue, vue-i18n, PrimeVue are peerDependencies (provided by ComfyUI)
- `@comfyorg/comfyui-frontend-types` provides TypeScript definitions
- External scripts: `../../../scripts/app.js`, `../../../scripts/domWidget.js`

### Internationalization
- Locales stored in `locales/{lang}/main.json`
- Use `useI18n()` hook with keys like `"vue-basic.title"`
- Components auto-register with vue-i18n instance

### Important Notes
- **Never** directly edit files in `js/` - these are build artifacts
- ComfyUI Frontend version 1.24.4+ required for ComponentWidget support
- Widget serialization is async and must handle temp file uploads
- Node size adjustment happens in `nodeCreated` lifecycle hook
- Uses **Bun** as package manager - all commands use `bun` instead of `npm`