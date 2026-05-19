- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 8, 3, 8, 6
Now I have a thorough understanding of the paper and both reviews. Let me compose the final consolidated review.

**Paper assessment summary**: The paper proposes DART, a diffusion-based autoregressive motion primitive model for real-time text-driven motion control. The method section is well-written and technically sound. The experiment sections (Sec. 4.1–4.3) are present as `\input` commands not expanded by the parser — this is a known parser artifact, not a paper deficiency.

Let me verify all claims carefully against the paper text before including them.

---

**Verification of key reviewer claims:**

The harsh critic claims "the paper does not report the wall-clock time or number of optimization steps for the control tasks" — the optimization algorithm (Alg. 2) only shows the loop structure without specific iteration counts or timing. However, the optimization experiments are in the unparsed `\input` section, so I cannot confirm they lack this.

The harsh critic claims "scheduled training...is mentioned but not described in detail" — line 135 says "we use scheduled training...to progressively introduce the test-time distribution of the history motion." It's briefly described with citations. This is appropriate for the main text.

The strict critic claims "CLIP embeddings...are not specifically fine-tuned for motion" — line 130 confirms CLIP is used. This is a design speculation, not a verified flaw.

The paper explicitly acknowledges the coarse-annotation limitation (lines 278–280), so the harsh critic's related point #2 is partially addressed.

---

Now I'll write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
(none)

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion

## Removed Points
...with justification

## Novel Insights
...

## Suggestions
...
