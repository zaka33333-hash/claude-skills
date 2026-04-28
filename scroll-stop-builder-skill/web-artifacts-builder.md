---
name: web-artifacts-builder
description: >
  Creates elaborate multi-component web applications and interactive HTML artifacts using React,
  TypeScript, Tailwind CSS, and shadcn/ui. Bundles everything into a single self-contained HTML file.
  Trigger when the user needs a complex interactive tool, calculator, dashboard, product finder,
  configurator, or multi-component web app. Also triggers for "build an interactive tool",
  "create a web app", "make a configurator", "build a React component", or any complex UI
  that needs more than static HTML/CSS.
keywords:
  - React
  - TypeScript
  - web app
  - interactive tool
  - dashboard
  - calculator
  - configurator
  - shadcn
  - Tailwind
  - artifact
---

# Web Artifacts Builder Skill

You build sophisticated multi-component web applications using a modern React stack, then bundle them into a single HTML file that can be used anywhere.

---

## Technology Stack

- **React 18** + **TypeScript** — component framework
- **Vite** — development build tool
- **Tailwind CSS 3.4.1** — utility-first styling
- **shadcn/ui** — 40+ pre-built accessible components (built on Radix UI)
- **Parcel** — bundles everything into one `bundle.html` file

---

## Workflow

### Step 1 — Initialize Project
```bash
bash scripts/init-artifact.sh my-project-name
cd my-project-name
```
This scaffolds a complete React + TypeScript + Vite + Tailwind project with shadcn/ui pre-configured.

### Step 2 — Develop
Edit files in `src/`:
- `src/App.tsx` — main component
- `src/components/` — individual components (use `@/components/` path alias)
- `src/lib/utils.ts` — utility functions

### Step 3 — Bundle
```bash
bash scripts/bundle-artifact.sh
```
Produces `bundle.html` — a single file with all JavaScript, CSS, and dependencies inlined.

### Step 4 — Deliver
Share the `bundle.html` file. It runs standalone with no external dependencies.

---

## Available shadcn/ui Components

Pre-installed and ready to use:

**Layout**: Card, Separator, ScrollArea, AspectRatio, ResizablePanelGroup

**Forms**: Button, Input, Label, Textarea, Select, Checkbox, RadioGroup, Switch, Slider, Toggle, Form (react-hook-form)

**Navigation**: Tabs, Breadcrumb, NavigationMenu, Menubar, Pagination, Sidebar

**Feedback**: Alert, AlertDialog, Badge, Progress, Skeleton, Toast (Sonner), Tooltip

**Overlay**: Dialog, Drawer, HoverCard, Popover, Sheet

**Data Display**: Table, Avatar, Calendar, Chart (Recharts)

**Other**: Accordion, Collapsible, Command, ContextMenu, DropdownMenu

Import any component:
```typescript
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardContent } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
```

---

## Design Anti-Patterns to Avoid

The default shadcn/ui + Tailwind setup produces "AI slop" if used without intentionality:
- Avoid: everything centered, purple gradients, excessive rounded corners, Inter font for everything
- Do: pick a design direction first (see frontend-design.md), then implement it with the component library

---

## When to Use This vs. Plain HTML

| Use web-artifacts-builder | Use plain HTML/CSS |
|--------------------------|-------------------|
| Multiple interactive states | Static or near-static page |
| Data filtering, sorting, search | Simple form or layout |
| Charts and visualizations | Marketing/blog content |
| Complex forms with validation | Product page sections |
| Real-time calculations | Shopify liquid sections |
| 5+ components interacting | Single focused component |

---

## Example Use Cases for Star-Toner

- **Toner finder tool** — user selects printer brand/model → shows compatible cartridges
- **Cost calculator** — compare cost-per-page of original vs. compatible cartridges
- **Product configurator** — select cartridge type, yield, quantity → pricing summary
- **Compatibility checker** — enter printer model → see full list of compatible products
- **Audit dashboard** — display SEO audit findings in an interactive, filterable table

---

## Path Aliases

Use `@/` to reference `src/`:
```typescript
import { MyComponent } from "@/components/MyComponent"
import { formatCurrency } from "@/lib/utils"
```

Never use relative paths like `../../components/` — always use the `@/` alias.
