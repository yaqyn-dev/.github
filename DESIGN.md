# Organization profile design

The page introduces Yaqyn Development as an independent workspace for career projects. It complements the personal profile without repeating the learning-project gallery, credentials, or biography.

Use one static masthead, a left-aligned naturally wrapping 132 × 132 gallery, a project table, and three expandable case studies. Application repositories stay private; link to the approved HyperQuote and Modern showcases. Stockroom remains explicitly a private evaluation prototype.

## Identity

Black is the organization's primary brand color, chosen by the owner. The active
masthead is an original dust-and-typography bumper: particles clear to pure black,
`yaqyn.` appears in Montserrat Bold 700 above a smaller centered `dev`, the title
fades out, the email `contact@yaqyn.dev` fades in above `let's work`, then dust
returns while the contact card fades. The trajectory and opacity envelopes are
periodic for a continuous loop. The reference is the broad restraint of short
black-and-white television bumpers, not a copied logo or sequence.

Output is 1920 × 640 at a 25 fps motion cadence over 12 seconds. Identical held
frames are packed into longer frame durations without changing the timing.
Grayscale dust has varied focus, size, brightness and slow drift. Text positions
stay fixed; all transitions use smoothstep easing. No camera movement or zoom.

`yaqyn-dust-intro.gif` is rendered by `scripts/build_dust_cover.py`, with a matching
lossless WebP poster. The README uses the poster for reduced-motion preferences
and links the cover to it as a static alternative. Montserrat is bundled unchanged
under its OFL license; provenance is in `scripts/fonts/SOURCES.md`. Rendering
bakes the font into the assets, so visitors make no font requests.

Prior generated artwork is retained as an unused asset. The active masthead is
programmatic, with exact text and weight rather than generated letterforms.

The profile heading repeats the name as accessible text. Its table and prose carry the meaning independently of the artwork. Keep client metrics, team-size claims, and service guarantees out of the copy unless verified.

## Gallery and workflow

The organization is a career-work gallery, separate from the personal profile's learning and Linux projects. Keep the order HyperQuote, Modern, Stockroom in the card flow, table, and case studies. HyperQuote and Stockroom cards are original vector interpretations of their established blue palettes; Modern reuses its existing profile card unchanged. Cards are illustrations, not interface screenshots.

`hyperquote-preview.webp` is copied byte-for-byte from the approved public HyperQuote showcase (`docs/readme/screenshots/website-home.webp`). `modern-preview.webp` is copied unchanged from Modern's approved public services capture (`docs/readme/screenshots/services.webp`). Their original credits remain. All expanded screenshots belong inside project disclosures. Stockroom has no published interface capture or private-source link.

Section icons copy the exact canonical paths in the workspace `readme-style/icons.json`: career, workflow, verification, skills, AI, and contact. Render with white 1.6-unit rounded strokes and black backing; use 24px at H2 and 20px at H3. Decorative icons have empty alt text.

Use a GitHub note for public/private and prototype boundaries, a neutral Mermaid diagram for the development loop, tables for comparison, and collapsible case studies for depth. Do not add badge walls or decorative Markdown features without a reader purpose. The workflow describes the developer's approach, not a service guarantee. Verification examples distinguish configured checks from successful runs and production proof.
