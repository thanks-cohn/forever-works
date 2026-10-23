# Consumer Presentation Preservation — draft 0.1

Status: first documentation specification, requested by the owner on 2026-10-23. The owner has requested preservation of current UX/UI, intended consumer presentation, effects, animation, sound, fonts, structure, spacing and aesthetic resemblance. The detailed capture procedure below is agent-proposed for iteration. This does not change Standard 0.1, schemas, record kinds, evaluation algorithms or Public API v0.1. No automatic capture tool or completed product audit is claimed.

## Purpose

Preserve the product as the consumer experiences it, alongside the workings that produce it. A repository's full inventory is different from its consumer-facing product. Hidden experiments, developer tools and unfinished capabilities must not silently become part of the intended presentation.

Presentation can be an essential purpose: a successor that retains file transfer but loses the deliberate interaction, atmosphere, clarity and pleasure may fail the product's preservation goals. Cosmetic modernization is not sufficient justification for discarding accepted presentation obligations.

Use the [capture template](../templates/CONSUMER_PRESENTATION_CAPTURE.md) for each project and repeat its surface and transition records as needed.

## Separate observation, intention and realization

Maintain three linked accounts: current observed presentation, explicitly accepted intended presentation, and the implementation producing each experience. Record deviations and proposed changes separately. Source declarations are evidence of configuration, not proof of rendered appearance. Screenshots establish a particular rendered state, not interaction or sound. Owner instructions establish intent, not implementation.

For every material statement record a stable local identifier, scope, observation date, product commit/build, platform/environment, provenance, evidence location and limits. Label observations as runtime-observed, source-declared, documentation-reported or unknown. Track intent separately as owner-explicit, inferred or agent-proposed, with acceptance source/date when available. These are capture labels, not new core provenance enum values. Preserve original evidence when assessments change.

An unobserved category is unknown. Mark absent only after a bounded inspection and identify that scope; mark not-applicable with a reason. Never infer silence from missing audio files, a font from its appearance alone, or implemented motion from an approved description. Defects remain observed defects, not automatically accepted design.

## Capture coverage

| Category | Required capture in this draft procedure |
| --- | --- |
| Product and audience | Consumer goals, intended impression, audience, task priorities, product vocabulary and presentation boundaries. |
| Visible surfaces | Entry points, screens, native menus, dialogs, overlays, tooltips, badges, notifications, onboarding, settings, permissions and external handoffs. Separate default, optional, gated, internal and historical surfaces. |
| Structure | Information hierarchy, grouping, ordering, navigation, reading flow, alignment, stacking, density, fixed/scrolling regions and persistent versus temporary UI. |
| Spacing and geometry | Measured units, padding, margins, gaps, dimensions, min/max sizes, grid, line lengths, radii, hit areas, clipping, overflow and alignment anchors. Distinguish measured values from estimates. |
| Typography | Font family and exact asset/version/hash where available, license, loading/fallback behavior, size, weight, line-height, tracking, case, numeric variants and text wrapping/truncation. |
| Visual styling | Palette, state colors, contrast, material/texture, borders, shadows, gradients, transparency, iconography, imagery, lighting, depth and theme variants. |
| Effects | Trigger, target, visual layers, color/intensity/opacity, duration, fade, compositing, restoration and simultaneous-event behavior. Capture the ordinary state before and after. |
| Animation and transitions | Start/intermediate/end states, paths, anchors, duration/delay, easing or spring parameters, sequencing, overshoot, interruption/reversal, repetition, frame samples and reduced-motion behavior. |
| Sound and haptics | Event mapping, asset identity/license/hash, volume/envelope, duration, latency, repetition/overlap, mute/defaults, permission/autoplay dependencies and non-audio equivalents. Record unknown or scoped absence honestly. |
| Interaction | Mouse, touch, keyboard, focus, selection, hover, drag, shortcuts, dismissal, undo/cancel, disabled behavior and state persistence. |
| Content and feedback | Exact important labels, tone, helper text, status wording, progress semantics, validation and distinctions between queued, completed, partial, uncertain and failed. |
| State coverage | Initial, normal, hover/focus/pressed, selected, disabled, empty, loading, progress, success, partial, failure, offline, expired authentication and recovery, where applicable. |
| Adaptation and accessibility | Viewport and content extremes, zoom, device scale, orientation, input methods, long/localized/RTL text, screen readers, contrast, color-independent meaning, reduced motion and sound alternatives. Preserve hierarchy and aesthetic quality across sizes. |
| Performance and timing | Responsiveness, perceived delay, progress update cadence and resource limits affecting the experience; record measured environment and thresholds separately from wishes. |
| Assets and portability | Original editable assets, exports, licenses, fonts, media, platform-owned UI limits, substitute rules and acceptable variation on successor platforms. |

## Most resembles ____

Every capture includes this exact heading. Record artistic styles, periods, materials, games, applications or other projects that the presentation most resembles. Name the particular screen, version, effect or asset and the dimensions of resemblance: typography, layout, palette, motion, sound, atmosphere or interaction.

Distinguish owner-declared inspiration from observer-perceived resemblance. Include references with access date and permissible evidence, confidence, differences and features that must not be imported. Comparisons orient a future maintainer; they do not replace measurements, grant rights to copy assets or prove historical influence. If no defensible comparison is known, write unknown instead of inventing a reference.

## Connect experience to workings

For each journey, connect consumer goal → visible starting state → action → internal transition/capability → feedback → visible outcome and recovery. Link exact capability/invariant/implementation/evidence IDs when they exist, and versioned source anchors. For presentation without a backend effect, record that local state change explicitly. For hidden implementation work, identify whether any consumer surface exposes it.

Capture mismatches between visible claims and actual completion. A celebratory effect or counter must have a documented qualifying event; an HTTP acknowledgement alone must not be silently equated with completed delivery. Backend success also does not prove correct feedback, animation or layout.

Each intended obligation states what must survive, why it matters, permissible variation, applicable platforms, acceptance procedure and current verification result. Preserve exact geometry where identity requires it; elsewhere define relationships and bounded variation. Resolve conflicting owner directions through dated decisions rather than selecting whichever screenshot is newest.

## Evidence and verification

1. Pin artifact/build and configuration; inventory all consumer surfaces and gates. Record unavailable environments. Use synthetic or redacted data for captures.
2. Capture still images for stable states and recordings for transitions; capture audio independently when relevant. Include dimensions, scale, theme, font-loading state, inputs and reproducible steps. Preserve assets and checksums alongside evidence indexes.
3. Measure styles and timings where possible. Label source-derived declarations separately from observed output. Keep original observations when recording defects or intended corrections.
4. Replay journeys, including interruption, failure and recovery, at representative supported sizes and content extremes. Compare structure, typography, spacing, state meaning, timing, motion, audio and usability against scoped accepted obligations.
5. Report pass, fail or unknown for each obligation with evidence. Static document checks and screenshot similarity do not establish functional, temporal, audio or accessibility correctness. Missing evidence remains unknown; incomplete verification cannot establish full preservation.
6. Have an unfamiliar agent attempt a bounded reconstruction using the presentation package and capability contracts without the original UI source. Independently compare the result. Report source-assisted and source-independent results separately.

Record comparison tolerances and masks for dynamic content, font rasterization and native UI before accepting results. Retain human review for aesthetic judgments; document who judged what and why. No universal pixel threshold proves the intended experience survives.

## Adoption and model integration

Start with Markdown, evidence assets and a portable index. Existing intent, capability, invariant, constraint, decision, implementation and evidence records can express accepted obligations and their proof. If structured capture metadata is embedded in a core record, put it under an owner-qualified extensions key and preserve existing required fields and provenance. Local capture identifiers are not automatically canonical model references or native trace edges.

A future normative profile requires versioned schemas, valid/invalid fixtures, interoperable implementations and verification of unknown/failure behavior. Until then, this draft documents a proposed preservation workflow; it does not certify any project or extend the official API.

## REDOWN starting boundary

The documentation-only review of REDOWN commit 31fdbee412361c1d4e01d24929960e6e39aa1a84 reports temporary toolbar success/failure effects, delivery-counter motion, menu/Explorer surfaces, quiet defaults and reduced-motion obligations. These are documentation reports, not fresh runtime observations. Fonts, exact spacing, animation timings, sound presence and complete appearance remain unknown in this attempt. No REDOWN implementation was inspected for this specification.

The next project capture should preserve those distinctions and gather scoped runtime evidence before claiming a complete current presentation. A standard template is not a completed inventory.
