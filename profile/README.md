<img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/yaqyn-cover.webp" width="2171" height="724" alt="Yaqyn Development — sculptural white yaqyn. wordmark on black">

# Yaqyn Development

**Business software, built around the work.**

The career-project gallery and development workspace of **[Abdulrahman M. Yaqyn](https://github.com/yaqyn)**. Connected procurement, bilingual websites, and warehouse tools live here, with a common concern: making the next person's work clear.

An accounting background shapes the approach to records, responsibilities, and operational handoffs. Requirements come from the people doing the work; implementation has to account for what happens between the screens.

[Explore the portfolio](https://yaqyn.dev/) · [Personal projects and open source](https://github.com/yaqyn) · [Discuss a project](mailto:contact@yaqyn.dev)

## <img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/icons/career.svg" width="24" height="24" alt=""> Career projects

<p align="left">
  <a href="https://github.com/yaqyn/HyperQuote"><img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/projects/hyperquote.svg" width="132" height="132" alt="HyperQuote — connected procurement and delivery"></a>
  <a href="https://github.com/yaqyn/Modern"><img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/projects/modern.svg" width="132" height="132" alt="Modern — bilingual construction company website"></a>
  <a href="https://github.com/yaqyn-dev#stockroom"><img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/projects/stockroom.svg" width="132" height="132" alt="Stockroom — private warehouse workflow prototype"></a>
</p>

| Project | Engineering focus | Explore |
| --- | --- | --- |
| **HyperQuote** | Procurement, shared operational records, role-specific workspaces, and delivery coordination. | [Showcase](https://github.com/yaqyn/HyperQuote) · [Website](https://www.hyperquote.net/) |
| **Modern** | English and Arabic interfaces, service discovery, project galleries, and contextual inquiries. | [Showcase](https://github.com/yaqyn/Modern) · [Website](https://www.moderngroupco.com/) |
| **Stockroom** | Receiving, storage suggestions, confirmed transfers, and inventory movement history. | Private evaluation prototype |

> [!NOTE]
> Application source remains private. HyperQuote and Modern have public showcases. HyperQuote uses fictional data and shared demo accounts. Stockroom is a local evaluation prototype, not a production inventory system.

<details>
<summary><strong>HyperQuote · From a material request to a coordinated delivery</strong></summary>

<img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/hyperquote-preview.webp" width="1200" alt="HyperQuote's public website showcase, with material discovery and project planning">

A material request passes through several teams. HyperQuote connects customer planning, quotation revisions, stock, payments, dispatch, and the driver's delivery experience around shared records.

- **Customer planning:** material lists, editable drafts, quote requests, and order updates.
- **Operational handoffs:** workspaces for sales, inventory, finance, and dispatch.
- **Lyon assistance:** natural-language planning and information retrieval within the user's available context. Estimates remain editable and require review.

**Built with:** TypeScript · React · TanStack Start · Supabase · PostgreSQL · Cloudflare Workers

[Read the showcase](https://github.com/yaqyn/HyperQuote) · [Explore the customer portal](https://portal.hyperquote.net/)

</details>

<details>
<summary><strong>Modern · From service discovery to a useful inquiry</strong></summary>

<img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/modern-preview.webp" width="1200" alt="Modern's service interface, with discipline selection and a request-service action">

The website connects a construction company's services and project portfolio to a structured inquiry. A visitor can carry the service or project they were exploring into the contact experience.

- **Bilingual navigation:** English and Arabic, with both reading directions and light/dark themes.
- **Connected discovery:** service disciplines, project filters, and portfolio galleries.
- **Contextual intake:** the inquiry retains the visitor's selected service or project.

**Built with:** TypeScript · React · TanStack Start · Tailwind CSS · i18next · Cloudflare Workers

The materials marketplace remains in preparation. The public showcase documents selected interface states.

[Read the showcase](https://github.com/yaqyn/Modern) · [Visit Modern](https://www.moderngroupco.com/) · [View the animated brand cover](https://raw.githubusercontent.com/yaqyn/Modern/main/docs/readme/cover-story.gif)

</details>

<a id="stockroom"></a>
<details>
<summary><strong>Stockroom · Testing the warehouse workflow before integration</strong></summary>

Stockroom explores barcode-guided receiving, storage-place suggestions, and internal transfers in a local warehouse prototype.

```text
Receive stock → Suggest a place → Confirm the movement → Keep its history
```

A suggestion leaves stock unchanged. Confirmation rechecks capacity and contents, then records the balance change and its audit history together. Request identifiers protect unchanged retries from becoming duplicate movements.

**Current implementation:** Python · SQLite · Browser JavaScript

Authentication, Odoo integration, and production operation are outside the current prototype. Source and internal materials remain private.

</details>

## <img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/icons/workflow.svg" width="24" height="24" alt=""> Development workflow

**Understand the handoff before designing the screen.** The starting point is a concrete task: who initiates it, which records change, who acts next, and what should happen when an action fails.

```mermaid
flowchart LR
    B[Brief] --> M[Model]
    M --> I[Implement]
    I --> V[Verify]
    V --> D[Deliver]
    V --> I
    classDef stage fill:#000000,color:#ffffff,stroke:#777777
    class B,M,I,V,D stage
    linkStyle default stroke:#777777
```

| Stage | What it makes clear |
| --- | --- |
| **Brief** | The user's task, the operating constraints, and the intended result. |
| **Model** | Records, responsibilities, state transitions, permissions, and failure cases. |
| **Implement** | Interfaces and server behavior that follow the same rules. |
| **Verify** | Relevant automated checks and direct inspection of the complete journey. |
| **Deliver** | Documentation, deployment configuration, and the remaining operating requirements. |

The loop back from verification is deliberate: a failed check or confusing interaction sends the change back for revision.

## <img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/icons/verification.svg" width="24" height="24" alt=""> Verification follows the risk

Different projects need different evidence. A visual change, a stock movement, and a deployment change should not all receive the same check.

| Project | Examples of the checks behind the work |
| --- | --- |
| **HyperQuote** | Formatting, type checks, tests, repository consistency, and security scans in the project's check workflow. |
| **Modern** | Public-export boundaries, image references, and documentation checks; application type checks and builds in its deployment workflow. |
| **Stockroom** | Receiving and transfer behavior, capacity rejection, mixed-product rejection, and duplicate-request handling. |

Local checks, CI results, and live behavior are separate evidence. A successful push alone does not prove the deployed result.

## <img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/icons/skills.svg" width="24" height="24" alt=""> Tools behind the work

| Area | Tools in these projects |
| --- | --- |
| **Interfaces** | TypeScript, React, TanStack Start, Tailwind CSS, i18next |
| **Application data** | PostgreSQL, Supabase, SQLite, SQL |
| **Warehouse prototype** | Python, browser JavaScript |
| **Delivery and verification** | Git, GitHub Actions, Cloudflare Workers, automated checks, project documentation |

### <img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/icons/ai.svg" width="20" height="20" alt=""> AI in the development process

**Claude Code and Codex** support implementation, debugging, and review. Tasks start with requirements and repository context, then move through scoped changes, review, and verification. Design decisions and the resulting work remain my responsibility.

## <img src="https://raw.githubusercontent.com/yaqyn-dev/.github/main/profile/assets/icons/contact.svg" width="24" height="24" alt=""> Start with the workflow

For a project conversation, email **[contact@yaqyn.dev](mailto:contact@yaqyn.dev)** with the task, the tools currently involved, and the outcome you want to improve.

[Explore the portfolio](https://yaqyn.dev/) · [Meet the developer](https://github.com/yaqyn)
