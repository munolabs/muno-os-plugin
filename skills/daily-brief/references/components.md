# Daily Brief - Component Catalog

Reference for generating HTML content in daily-data.json sections.
All components use the design system defined in template.html.

## Stat Cards

Use in the `stats` array of daily-data.json. Rendered as a top-level grid.

```html
<div class="stat-card">
  <span class="label-muted">Label here</span>
  <span class="stat-value teal mono">$4.250,30</span>
  <span class="stat-delta up">+$12,50 vs ayer</span>
</div>
```

Colors for `.stat-value`: `teal`, `blue`, `red`, `yellow` (or none for white).
Colors for `.stat-delta`: `up` (green), `down` (red), or none (muted).

## Alerts

Use in the `alerts` array. Rendered below stat cards.

```html
<div class="alert warning">
  <span class="alert-icon">!</span>
  <div class="alert-body">
    <div class="alert-title">Title here</div>
    <div class="alert-desc">Description here</div>
  </div>
</div>
```

Types: `alert` (red), `alert warning` (yellow), `alert info` (teal).

## List Items

For tasks, emails, generic lists inside section `content_html`.

```html
<div class="item">
  <div class="item-icon">1</div>
  <div class="item-body">
    <div class="item-title">Task title</div>
    <div class="item-meta">Context or metadata</div>
  </div>
</div>
```

## Timeline

For agenda/calendar sections.

```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-time">09:00</div>
    <div class="timeline-dot meeting"></div>
    <div class="timeline-content">
      <div class="timeline-title">Meeting title</div>
      <div class="timeline-sub">With person - 30 min</div>
    </div>
  </div>
</div>
```

Dot types: default (teal), `.meeting` (blue), `.task` (yellow).

## Badges

Inline status indicators.

```html
<span class="badge badge-teal">Active</span>
<span class="badge badge-blue">In Progress</span>
<span class="badge badge-yellow">Warning</span>
<span class="badge badge-red">Overdue</span>
<span class="badge badge-muted">5 items</span>
```

## Cards

Container for sections.

```html
<!-- Bordered card (primary sections) -->
<div class="card">
  <div class="card-header">
    <span class="label">Section Title</span>
    <span class="badge badge-muted">3 items</span>
  </div>
  <!-- content here -->
</div>

<!-- Flat card (secondary sections) -->
<div class="card-flat">
  <!-- content here -->
</div>
```

## Cashflow / Key-Value Rows

For financial data or any label-value pairs.

```html
<div class="cf-row">
  <span class="cf-label">Revenue</span>
  <span class="cf-value positive">$12,500,000</span>
</div>
<div class="cf-row">
  <span class="cf-label">Expenses</span>
  <span class="cf-value negative">-$8,200,000</span>
</div>
```

Value colors: `.positive` (teal), `.negative` (red), `.neutral` (white).

## Project Rows

For project listings.

```html
<div class="project-row">
  <span class="badge badge-teal">Active</span>
  <span class="project-name">Project Name</span>
  <span class="project-owner">Owner</span>
</div>
```

## Progress Bar

```html
<div class="progress-bar">
  <div class="progress-fill" style="width: 65%"></div>
</div>
```

## Layout Helpers

```html
<div class="grid-2"><!-- 2 columns --></div>
<div class="grid-3"><!-- 3 columns --></div>
<div class="grid-4"><!-- 4 columns --></div>
<div class="stack"><!-- vertical stack with gap --></div>
<div class="row"><!-- horizontal flex with gap --></div>
<div class="spacer"></div><!-- 28px vertical space -->
<div class="divider"></div><!-- thin horizontal line -->
```

## Section Title

Used to separate major sections.

```html
<div class="section-title">
  <span class="label">Section Name</span>
</div>
```

The `::after` pseudo-element adds a horizontal line that extends to fill the row.

## Typography

- `.label` -- uppercase, teal, 10px (section headers)
- `.label-muted` -- uppercase, muted, 10px (card sub-headers)
- `.mono` -- monospace font (numbers, values)
- `h1` -- 22px bold (page title)
- `h2` -- 13px semibold (card titles)
- `p` -- 13px soft color (body text)
