Now I have enough information. Let me write the final review. Let me carefully assess the paper's core position and the strength of its argumentation.

The key tension: The paper makes a very strong claim — "AI systems whose behavior cannot be explained even by their creators are fundamentally incompatible with due process" — but its own evidence and analysis suggest a more nuanced, conditional position. Let me assess each of the harsh critic's claims:

1. **"Fundamental incompatibility" claim undermined by own evidence**: This is partially valid. The paper does say "fundamental incompatibility" (bold, Section 3), but it also explicitly says "some methods are more salvageable than others" (Section 4) and "Banning the tools doesn't make sense, but requiring extreme transparency in their use for budget determinations does" (p. 82). The paper further states in Section 6 that due process provides a "checklist for acceptable AI-driven behavior" — implying some AI systems could satisfy it. This is a real tension, though not a fatal one — the paper could be read as saying AI systems *in their current form* are fundamentally incompatible, and that simpler models *with adequate transparency* could potentially satisfy due process requirements. The paper's abstract actually says "AI in its current form cannot guarantee due process, and therefore cannot and (should not) be used." This is more conditional than "fundamentally incompatible forever." However, the bold claim in Section 1 and Section 3 doesn't include this qualification, and the tension between the bold claim and the nuanced discussion in Section 4 is real.

2. **Failure to engage with human comparison**: This is a valid criticism. The paper mentions in passing that "courts have shown a troubling tendency to think of AI systems as inherently mathematical and therefore 'unbiased' and superior to inevitably biased human decision-makers" (Section 2), and Section 5 briefly mentions advocates saying AI "are still faster and less problematic than the alternative human decision makers (judges)" — dismissed in one sentence. The paper doesn't seriously engage with this objection.

3. **Technical sections disconnected from legal argument**: This is partially valid. The paper does say "some methods are more salvageable than others" but doesn't clearly specify the boundary. However, it does gesture toward this ("A logistic regression would perhaps have to be explained by a feature importance ranking..." p. 76-80), and the Coca-Cola analogy and Section 6's "checklist" do offer some guidance.

Let me now write the review.</think>Now I have all the calibration data and close reading needed. Let me write the final review.

## Summary

This position paper argues that current AI systems are fundamentally incompatible with constitutional due process protections because even their creators cannot fully explain the "why" behind their decisions, and trade secret protections block external scrutiny. Using two case studies (disability rights in *KW v. Armstrong* and criminal sentencing in *State v. Loomis*), the paper argues that AI-driven decision-making violates the notice and hearing requirements of due process, and that the ML research community must engage more directly with legal institutions to restore these protections.

## Strengths

- **Productive identification of the "not determinative" logical problem in *State v. Loomis***: The paper exposes a sharp structural contradiction: if a COMPAS risk score is not significant enough to affect the decision, there is no reason to use it; if it is significant, it should be subject to scrutiny. "It must be one or the other" (Section 4.6). This is one of the paper's most incisive observations and directly invites productive disagreement.

- **Novel Coca-Cola trade secret analogy**: Section 4.7 offers an original, well-constructed comparison — Coca-Cola's formula is a trade secret, yet the company must provide ingredient lists and nutrition labels. The paper uses this to argue that trade secret protection should not exempt AI systems from minimum disclosure requirements. This is a genuinely useful frame that moves the discussion beyond prior work on trade secrecy.

- **Effective pairing of contrasting case studies**: *KW v. Armstrong* (where trade secret protections were overruled and the system's flaws were revealed) vs. *State v. Loomis* (where protections were upheld, blocking any scrutiny) demonstrates that current legal frameworks produce inconsistent outcomes for similarly vulnerable populations, making a compelling case for systemic reform.

- **LLM self-explanation as a novel due process threat**: Section 4.3 identifies a distinct risk — laypersons will mistakenly credit LLM-generated natural-language explanations as fulfilling the "notice" requirement of due process, when these explanations are "meaningless and often false while seeming very believable on the surface." This distinguishes the paper from earlier due process scholarship focused on simpler scoring tools.

- **Concrete action agenda for ML researchers**: Section 7 provides five specific tasks (e.g., "investigate how much information we need to thoroughly interrogate and evaluate models, and develop new techniques for doing so that can protect *some* degree of proprietary protections"), making the paper a genuine call to action rather than merely diagnostic.

## Weaknesses

### Major

- **Internal tension between the categorical "fundamental incompatibility" framing and the paper's own more nuanced analysis**: The paper stakes its position on the bold claim that AI systems "are fundamentally incompatible with [due process]" and that incompatibility "cannot be remedied simply through additional transparency requirements" (Section 3). Yet the paper itself says "some methods are more salvageable than others" (Section 4 intro), that "Banning the tools doesn't make sense, but requiring extreme transparency in their use for budget determinations does" (p. 82), and Section 6 proposes due process as a "minimum checklist for acceptable AI-driven behavior" — implying some AI systems could satisfy it. This is not a minor framing issue: it directly affects whether the paper's position calls for a blanket prohibition or targeted regulation, and the paper's evidence supports the latter more convincingly than the former. The abstract's qualifier ("AI in its current form") partially addresses this, but the bolded thesis statement in Section 1 and the categorical language in Section 3 do not.

- **Insufficient engagement with the strongest counterargument — that human decision-makers also systematically violate due process**: Section 5 acknowledges that "certain advocates" argue biased AI systems "are still faster and less problematic than the alternative human decision makers (judges)" but dismisses this in a single sentence without analysis. This is the most important objection to the paper's "should not be used" position. Human decision-makers notoriously provide post-hoc rationalizations driven by implicit bias, and the paper itself notes that courts assume humans are more biased than AI (Section 2). The paper needs to explain why AI's due process failures are categorically different in kind from the known failures of human decision-makers, rather than merely asserting that they are.

### Minor

- **The model-type taxonomy in Section 4 does not explicitly map to a due process compatibility standard**: The paper discusses regression, neural networks, LLMs, CART, and statistical tools, acknowledging varying interpretability, but never specifies which model types it considers fundamentally incompatible with due process versus which could be compatible under appropriate transparency requirements. The phrase "some methods are more salvageable than others" gestures toward a boundary but does not draw one.

- **Section 5 ("Alternative Views") is too brief**: It gestures at three alternative positions (ironclad trade secrets, AI being better than biased judges, and courts' own views) without substantively engaging with any of them. The observation of a "gap" between the ML and legal communities is valuable but reads as an observation rather than an argument.

## Trivial

None.

## Nice-to-Haves

- A clearer statement of where the compatibility boundary lies — e.g., a conditional position such as "AI systems that cannot provide meaningful notice and cannot be meaningfully contested are incompatible with due process; current trade secret law and model opacity create conditions where many deployed systems fail this test" — would sharpen the paper's contribution and make it more productive for debate.

- A systematic (even brief) comparison of how due process failures differ under AI vs. human decision-making, to strengthen the "should not be used" normative claim.

## Removed Points

- **"The paper fails to empirically prove its position" / "absence of empirical results"**: This is a position paper making a normative and conceptual argument supported by legal case studies. Empirical validation is not required for the kind of argument it makes, and the paper explicitly calls for future empirical work (Section 7, item 1). Removed.

- **"Not yet released" / unverifiability concerns about cited works**: Cited works, datasets, and models are assumed to exist per instructions. Removed.

- **"Overclaiming" / "too provocative" / "insufficiently hedged"**: Position papers are expected to make strong, provocative claims. The "fundamental incompatibility" framing is the paper's stated position — a debatable stance that invites productive disagreement. The only issue worth keeping is the *internal tension* between this framing and the paper's own more nuanced analysis, which I retained as a Major weakness. Removed as a standalone criticism.

- **"Section-by-section notes about lawyers being woefully unprepared" / "asserted rather than demonstrated"**: The claim that lawyers lack technical AI expertise to challenge AI systems is well-supported by the case studies (courts unable to understand COMPAS, Justice Abrahamson saying "the court needed all the help it could get"). This is demonstrated, not merely asserted. Removed.

- **"Case study 1 isn't really about modern AI" / "sounds like a badly implemented regression"**: The case study's point is that even simple statistical tools used in high-stakes decisions can violate due process — this actually strengthens the paper's broader argument. The nature of the model type is part of the problem the paper identifies. Removed.

- **"COMPAS problems stem primarily from trade secret law, not technical opacity"**: This is exactly the paper's two-barrier argument — that *both* interpretability limitations and trade secret protections create the incompatibility. The paper explicitly discusses both barriers throughout. Removing one barrier (trade secrets) would address some but not all of the problem, per the paper's own argument that even with transparency, the "why" of complex models remains elusive. The harsh critic's point about this not being fully analyzed is partially valid but already captured in the Minor weakness about the model-type taxonomy. Removed as a standalone Major.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Adopt the conditional framing explicitly in the thesis statement: "AI systems that cannot meaningfully explain their decisions and cannot be meaningfully contested are incompatible with due process" — and argue *that* some currently deployed systems meet this standard. This makes the paper's evidence fully support its position while still advancing a strong, debatable claim.

- Expand the "Alternative Views" section to engage with the human vs. AI comparison substantively, explaining why AI opacity presents a distinctive category of due process failure (e.g., scale, consistency of errors, inability to cross-examine) rather than merely a different flavor of the same problem.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Decision | Comparison |
|-------|-----------|----------|------------|
| PFRandBfSz (AI innovation vs. fundamental rights, EU AI Act model) | 7.0 | Accept (Oral) | Similar topic rights-based AI regulation position; this paper has a stronger central argument (Loomis contradiction, Coca-Cola analogy) but weaker engagement with counterarguments and internal tension in its framing |
| DS1XSAPvKs (Refutations & Critiques track) | 7.0 | Accept (Oral) | Clearer position, more actionable proposal; this paper has comparable practical utility but less internally consistent framing |
| 0TRVB5ghCR (plausibility is invalid for XAI) | 5.0 | Reject | Similar pattern of strong claim undermined by internal tension; this paper's evidence is stronger and case studies are more substantive |
| Omq9tUouSS (symbolic rules can't constrain learning) | 3.67 | Reject | Much weaker argumentation, no empirical examples; this paper is substantially stronger |
| g8Fo6qtnMR (expert orchestration vs. monoliths) | 4.0 | Reject | Internal contradictions weaken the central claim; this paper has similar but less severe tension |
| 8ZH52QHIZV (X in XAI not useful) | 5.33 | Reject | Provocative claim with thin evidence; this paper has stronger evidence base from case studies |

This paper has genuinely important insights (the Loomis logical contradiction, the Coca-Cola analogy, LLM self-explanation as a due process threat) and real institutional value in bridging ML and legal communities. Its Major weaknesses — the internal tension between "fundamental incompatibility" and the conditional analysis, and the thin engagement with the strongest counterargument — are addressable in revision and do not undermine the paper's core contribution. The paper is clearly stronger than papers scoring 4-5 (it has substantive case studies and clear policy implications) and slightly weaker than the top-scoring position papers (which have more internally consistent arguments and fuller counterargument engagement).

MY FINAL SCORE: <pineapple>6</pineapple>
MY FINAL DECISION: <orange>Accept</orange>