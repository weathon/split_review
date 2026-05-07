Now I have a thorough understanding of the paper and calibration anchors. Let me compose my final review.

## Summary

This position paper argues that the crisis in human data quality for AI stems not from LLM contamination alone but from fundamentally flawed data collection design that prioritizes extrinsic incentives (speed, pay, control) at the cost of contributors' intrinsic motivation, which drives the very shortcutting behavior (e.g., annotators using LLMs) that degrades data. It synthesizes Self-Determination Theory, Self-Perception Theory, and the Overjustification Effect into a causal account of motivational crowding-out in data work, introduces "resolution of control" as a design variable spanning environment-level to task-level control, and proposes games as a promising design paradigm that balances structured data collection with voluntary, intrinsically motivated participation.

## Strengths

- **Novel reframing of the data quality crisis as a motivational design failure.** The paper identifies a genuinely underexamined angle: the problem is not just LLM contamination but the incentive structures that make shortcutting rational for workers (Section 1: "the core issue is not new... the advent of LLMs has amplified these problems"; Section 5: crowdwork systems create "a vicious cycle where contributors prioritize efficiency over authenticity"). This reframing opens productive discussion beyond the current tactical focus on detecting synthetic content.

- **Effective theoretical synthesis across psychology, economics, and ML practice.** The paper chains Self-Determination Theory (autonomy, competence, relatedness), Self-Perception Theory (attribution shift), the Overjustification Effect (Lepper et al., 1973), and Goodhart's Law/Cobra Effect into a coherent causal narrative of why extrinsic incentives progressively degrade intrinsic motivation and data quality (Section 5). The preschool drawing experiment is used to particularly strong effect — showing that expected rewards reduce both voluntary engagement and output quality, directly paralleling annotator behavior.

- **The "resolution of control" as a conceptual design variable.** Section 7 introduces a useful axis from environment-level (low control, e.g., Wikipedia) to task-level (high control, e.g., MTurk), explaining why existing systems cluster at dysfunctional extremes and why medium-resolution design offers a better frontier. This provides a concrete vocabulary for future design discussions rather than an abstract aspiration.

- **Sharp distinction between compensation-as-acknowledgment and compensation-as-incentive.** Section 5 draws a clean line between pay that acknowledges value (which SDT predicts can be benign or even positive if informational) and pay that controls behavior (which triggers crowding-out). This is actionable: it tells designers what to avoid without rejecting compensation entirely.

- **Honest engagement with the limitations of the games proposal.** Section 8.2 acknowledges that "no data collection games in machine learning have yet demonstrated sustained success," notes ReCAPTCHA's erosion of trust, and explicitly lists design trade-offs. This invites productive disagreement rather than closing it down.

- **Vivid trust-erosion examples.** Section 7.3 on Stack Overflow protests and artist pushback against AI training makes the trust argument concrete and demonstrates how quickly fragile social contracts can collapse — an important cautionary note for any design proposal.

## Weaknesses

### Fatal
None.

### Major

- **The position does not explain how to create intrinsic motivation for inherently uninteresting data collection tasks.** The paper's core argument is that systems should "design for intrinsic motivation" rather than relying solely on extrinsic incentives. The primary evidence for this working comes from platforms (Wikipedia, Reddit, open-source) and scientific games (FoldIt, Zooniverse) where the tasks themselves have natural appeal — editing articles on topics you care about, classifying galaxies, folding proteins. But many ML data collection tasks — bounding box annotation, toxicity labeling, preference ranking — lack any inherent intrinsic appeal. The paper acknowledges that "well-designed incentives can serve as catalysts for behaviors that might not otherwise occur" (Section 5), but this concession is not reconciled with the main design recommendation. The games proposal (Section 8) works best when the game mechanic can make a task engaging, but the paper does not explain how to gamify, say, repetitive safety annotation. Without addressing the hardest case — tasks where no natural intrinsic motivation exists to either protect or design for — the position applies to a narrower slice of data collection than it claims.

- **The Wikipedia/Reddit comparison as evidence is confounded by self-selection effects.** Throughout the paper (Sections 3, 5, 7), Wikipedia and Reddit are presented as existence proofs that intrinsic motivation sustains high-quality, high-quantity data. But this comparison conflates motivational design with self-selection: Wikipedia editors choose to write about topics they already care about, and Reddit posters self-select into communities aligned with their interests. MTurk workers, by contrast, are assigned arbitrary tasks. The quality advantage may stem not from intrinsic motivation per se but from matching contributors to tasks they find meaningful. The paper does not address this confound, which weakens its primary empirical support. Acknowledging it would either strengthen the paper (by clarifying scope) or significantly narrow its claims.

### Minor

- **The "medium resolution of control" recommendation needs more mechanistic justification.** The paper argues that the ideal system sits in the middle of the resolution-of-control spectrum (Figure 4), balancing autonomy and structure. But the mechanism by which medium control preserves intrinsic motivation is underspecified. SDT's logic pushes toward *more* autonomy (less control is better), while the paper claims the middle is optimal. The explanation — "too little control = incoherence, too much = motivational collapse" — is intuitive but not derived from the psychological theory the paper draws on. A mechanism-level account of why the sweet spot is in the middle, rather than maximally autonomous, would strengthen the framework.

- **The "naturalness" quality criterion is underspecified for safety-critical annotation.** Section 4 proposes anchoring quality in "naturalness" — how people behave without interference. For training models of human behavior, this has merit. But for safety-critical annotation (medical labeling, content moderation), what we want is deliberate, careful judgment — precisely the opposite of unprompted, routine behavior. The paper does not clarify when naturalness is the right criterion and when it is not.

- **The "enough money" counterargument from behavioral economics is not engaged with.** Research suggests that sufficiently high and well-structured extrinsic rewards can sustain quality even without intrinsic motivation, particularly for expert tasks. The paper assumes crowding-out is the dominant dynamic, but for well-paid specialized annotation, this may not hold. Addressing this counterargument — even to explain its limits — would strengthen the position.

### Trivial
None.

## Nice-to-Haves

- A typology distinguishing data collection tasks by how "gamifiable" or intrinsically motivating they could plausibly be (e.g., image tagging = high; toxicity labeling = low; domain-expert annotation = already motivating) would help scope the position's applicability and focus design efforts where they matter most.
- Analysis of why GWAP-era game-based data collection didn't sustain momentum in ML, even for the tasks where it initially succeeded, would strengthen the argument that a renewed effort can succeed.
- Engagement with hybrid approaches where games handle quantity while targeted human annotation handles quality-sensitive tasks.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Games haven't demonstrated viability at scale" as a Major weakness.** The paper explicitly acknowledges this limitation (Section 8.2: "no data collection games in machine learning have yet demonstrated sustained success"). A position paper can legitimately argue for an approach that hasn't been fully tried yet; the paper's honesty about the gap is a strength, not a weakness. Downgraded to a Nice-to-Have (diagnosing why past efforts didn't sustain would strengthen the argument).

- **"Not enough empirical evidence" for the position.** This is a position paper arguing from theory, examples, and reasoning. Demanding controlled experiments showing crowding-out in crowdwork settings is applying standard research paper criteria to a position paper. The existing evidence — psychological theory, real-world platform comparisons, documented quality declines on MTurk, LLM use by annotators — provides adequate support for a debatable position.

- **"LLM-contamination framing loosely connected to the argument."** The connection is explicit and coherent: the paper argues LLM use by annotators is a *symptom* of motivational collapse caused by over-reliance on extrinsic incentives (Section 5: shortcutting behavior "such as automating their annotation tasks using AI... ultimately degrading data quality"). The paper deliberately reframes the LLM crisis as downstream of a motivational crisis — this is the paper's contribution, not a gap.

- **"Figure 2 places Wikipedia/Reddit above the frontier without argument."** The text does support the visual — Section 3 states these platforms "operate outside this trade-off" and the surrounding discussion explains why. The figure accurately represents the paper's claim.

- **"Overclaiming" or "too provocative" criticisms.** The paper uses forceful framing ("When Incentives Backfire, Data Stops Being Human"; the donkey metaphor) that is appropriate and expected for a position paper. No factual falsehoods or self-contradictions were identified.

- **"The paper is a literature review, not a position paper."** The paper clearly takes a position ("rethinking data collection systems to align with contributors' intrinsic motivations"), advocates for a specific design direction (games, medium resolution of control), and engages with counterarguments. It is genuinely a position paper.

- **Missing references/related works.** Per rules, I do not flag these.

## Novel Insights

The most novel contribution of this paper is the identification of "resolution of control" as an axis along which data collection systems can be analyzed and designed — moving beyond the simple "intrinsic vs. extrinsic" dichotomy to show that the *granularity* of control (environment-level vs. task-level) is itself a design variable with predictable failure modes at both extremes. This framing unifies observations about Internet data (too little control → incoherence) and crowdwork (too much control → motivational collapse) under a single explanatory lens, providing the community with a vocabulary for structured debate about where on this spectrum specific data collection efforts should fall.

## Suggestions

- Explicitly scope the position by task type: acknowledge that for inherently unrewarding annotation tasks, the recommended approach may require creative game-design solutions that remain speculative, and discuss whether some tasks may simply require well-structured extrinsic incentives rather than intrinsic motivation design.

- Address the self-selection confound head-on: clarify whether the paper's claim is that intrinsic motivation design *creates* motivation where none exists, or that it *preserves* motivation in self-selected contributors — these are different causal stories with different design implications.

- Provide a brief mechanistic account of why "medium" resolution of control is optimal rather than "maximal autonomy" — potentially by connecting to the concept of "optimal challenge" or "flow" from psychology, which could reconcile SDT's autonomy push with the need for structure.

## Calibration Summary

Anchors compared against:

| Paper | Avg Score | Relation |
|-------|-----------|----------|
| SbfjBNlJE7 (Collective bargaining for data workers) | 6.67 | Similar topic (ML data pipeline reform); stronger empirical grounding with worker survey, similar conceptual clarity |
| mdKzkjY1dM (Sustainable AI data deals) | 6.0 | Similar topic (data value chain); more rigorous empirical analysis (51 data deals) but similar abstraction level for proposed solutions |
| LAXgS0xzPf (Human expertise as data) | 5.33 | Partially similar (human data value); this paper has clearer position, better-defined terms, and a more novel framework |
| R6TXwNF1SB (Six pillars for AGI) | 3.0 | Low-scoring anchor; this paper is far stronger — coherent argument, defined terms, genuine position |
| PgA9rZoMY8 (Bidirectional Human-AI Alignment) | 8.0 | High-scoring anchor; more comprehensive framework, broader literature synthesis — this paper is narrower but comparably insightful |
| yqKfMr0yvY (LLMs-as-judges validity) | 7.67 | High anchor; similarly draws on measurement theory from psych — this paper's theoretical synthesis is strong but its empirical grounding is weaker |

This paper is stronger than LAXgS0xzPf (5.33) due to its clearer position, better-defined framework, and more honest scope limitations. It is weaker than the 6.67 collective bargaining paper due to the unaddressed scope limitation (uninteresting tasks) and the selection confound in its primary empirical support. It is comparable in quality to mdKzkjY1dM (6.0) but trades that paper's empirical rigor for a more novel conceptual framework. The theoretical synthesis and "resolution of control" framework are genuine contributions that justify a score above the borderline.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>