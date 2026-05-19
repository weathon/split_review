- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3
Now I have all the information needed. Let me construct the final review.

## Summary

This paper systematically evaluates off-the-shelf VLMs on three primitive skills underlying indoor scene layout synthesis: (S1) communicating spatial coordinates, (S2) reasoning about free space and collisions, and (S3) joint reasoning about free space, alignment, orientation, and functionality. Across five VLMs, five visual representations, and four coordinate representations (3400 questions), the study finds that normalized coordinates work best, that visual input surprisingly degrades performance relative to text-only, that free-space reasoning sits near chance, and that joint reasoning collapses to chance. The paper also demonstrates that tool-augmented collision checking yields perfect accuracy.

## Strengths

1. **Systematic decomposition of 3D layout reasoning into testable primitives.** The paper isolates three distinct skills (coordinate communication, free-space reasoning, joint reasoning) and designs controlled VQA tasks for each, enabling fine-grained diagnosis rather than end-to-end pipeline black-box evaluation. Evidence: Sections 3.1–3.3 define S1, S2, S3 with distinct question types and difficulty levels; the dataset spans 5 visual axes × 4 coordinate representations.

2. **Counterintuitive finding about visual input.** Multiple state-of-the-art VLMs perform *worse* with detailed 3D renderings than with simplified sketches or even no image at all. Evidence: Table 3 shows GPT-4o at 85.3% (no image) vs. 70.7% (3D1 top-down) and 69.3% (3D3 embodied); Table 2 shows similar patterns across models. This challenges the assumption that richer visuals improve spatial reasoning.

3. **Clean demonstration of tool-augmented spatial reasoning.** Offloading collision checking to a tool enables GPT-4o to achieve 100% accuracy on free-space reasoning with normalized coordinates, compared to ~74% without. Evidence: Table 4 reports GPT-4o accuracy of 1.00 for both normalized and absolute coordinates with tool usage. This provides actionable guidance for practitioners building VLM-based layout agents.

4. **Well-designed S3 task that forces genuine visual reasoning.** By withholding object sizes from the textual prompt (unlike S2), the S3 task ensures the model cannot solve the question via symbolic computation alone and must visually perceive object extent. The consistent chance-level performance across all models (Table 5) is a clean, reproducible result. Evidence: Section 3.3 lines 83–84 explicitly state the design rationale.

## Weaknesses

### Fatal
None.

### Major

1. **The S2 task design provides full textual information, making the headline "visual failure" claim from S2 require stronger caveating.** The paper explicitly acknowledges (line 68) that S2's textual description includes location and size of *both* existing and target objects, allowing purely symbolic collision computation. The finding that visual input *degrades* performance vs. text-only is genuinely interesting (measuring visual distraction or multimodal integration failure), but the abstract and introduction present the "10–20% worse when visual inputs are included" result (from S2) as direct evidence that VLMs "do not effectively utilize visual information" without adequately distinguishing it from the stronger S3 result where visual information is actually necessary. The paper partly mitigates this by designing S3 to force visual reasoning (lines 132–133), and the S3 results independently support the claim, but the framing of the S2 evidence in the abstract is imprecise. This is fixable with clearer language distinguishing the two sources of evidence.

### Minor

2. **No statistical precision estimates.** With 25 binary questions per condition for S1/S2 and 50 for S3, the standard error per condition is ~5–10 percentage points. Several between-condition differences discussed (e.g., 5–15 point gaps across visual axes in Table 3) could fall within noise, yet no confidence intervals, error bars, or significance tests are reported. This is common practice in LLM evaluation papers, but the paper would be meaningfully strengthened by adding bootstrap intervals or similar analysis.

3. **S3 lacks quantitative error decomposition.** The paper correctly reports that all models perform at chance on S3, but the error analysis is purely qualitative (line 142: scene graph hallucination, orientation misreasoning, etc.). A systematic breakdown of errors by type (collision vs. alignment vs. orientation vs. functionality) would reveal which specific skill failures drive the chance-level aggregate and would be more informative than the aggregate accuracy alone.

4. **S3 annotation subjectivity not quantified.** Inappropriate placements were manually annotated based on functionality, alignment, and collision criteria (lines 85–86). No inter-annotator agreement or detailed annotation rubric is reported. While the task is intrinsically somewhat subjective, a reliability measure would strengthen confidence in the ground-truth labels.

### Trivial
None.

## Nice-to-Haves

- **Controlling for object recognition.** The paper does not test whether VLMs can correctly identify the furniture items in the renderings. A model that misidentifies a dressing table as a nightstand will fail at functionality reasoning regardless of spatial ability. A quick auxiliary classification test would disentangle object recognition failures from spatial reasoning failures.
- **Error breakdown for S2 All-In condition.** Since the All-In condition renders both objects with visible collisions, reporting which mistakes are "false positive (says collision where none exists)" vs. "false negative (misses visible collision)" would strengthen the qualitative claim that models ignore visual evidence.

## Removed Points

- **"S1 is essentially arithmetic, overstating cognitive demand"** — Removed. The paper explicitly describes S1 as a "straightforward task" (line 58) and notes "this is perhaps to be expected since all answers can be computed with text only" (line 111). The criticism attributes a claim the paper never made.
- **"Tools experiment is tangential to the paper's main focus"** — Removed. The paper explicitly states (line 134): "While beyond the scope of visual reasoning that we aim to study in this paper, this experiment shows how practitioners could offload computation…" The authors are transparent about scope; the experiment is presented as a practical extension, not a core claim.
- **"Request for a visual-only S2 condition"** — Removed as a weakness. The paper already implements this via S3, which withholds object sizes from text to force visual reasoning. The reviewer's suggestion is already the paper's design choice.
- **"Prompt sensitivity should be reported across variations"** — Removed as a weakness. The paper reports (line 130–131) that multiple prompt phrasings and CoT were tested, and CoT "resulted in no performance change (Tab. 13)" in supplementary. The range of results is partially addressed.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a reframing or connection the paper itself does not already articulate.

## Suggestions

1. **Sharpen the framing of the S2 finding.** Distinguish clearly between: (a) "models favor symbolic computation even when visual evidence is available" (S2's actual evidence) and (b) "models cannot reason visually when symbolic computation is impossible" (S3's evidence). The abstract should not present the S2 visual-degradation result as unqualified evidence for (b).

2. **Add error bars or bootstrap intervals** to the main accuracy tables (especially Tables 2 and 3). With 25–50 binary samples per cell, this is inexpensive and would allow readers to assess which comparisons are reliable.

3. **Add a quantitative error-type breakdown for S3** (e.g., percentage of errors attributable to collisions vs. alignment vs. orientation vs. functionality) to accompany the qualitative analysis.
