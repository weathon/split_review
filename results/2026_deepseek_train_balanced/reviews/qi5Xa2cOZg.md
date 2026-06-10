Here is my final consolidated review:

---

## Summary

This paper proposes LGA (Language-Guided Abstraction), a framework that uses LLMs to automatically construct task-relevant state abstractions from natural language task descriptions. The pipeline has three modular stages: textualization (converting raw observations to text-based feature sets), feature abstraction (using an LM to select task-relevant features), and instantiation (rendering the abstracted features back into masked visual states). A policy is then trained on these abstracted states via imitation learning. Experiments on simulated tabletop tasks and a real Spot robot show that LGA achieves comparable performance to human-designed abstractions while requiring significantly less human specification time, and that the resulting policies are more robust to observational covariate shift and linguistic ambiguity than standard GCBC baselines.

## Strengths

- **Statistically significant reduction in human specification effort**: A controlled user study with 18 participants demonstrates that LGA and LGA-HILL require significantly less user time than manual feature specification (p < 0.001, paired t-test) across all tasks, while achieving comparable downstream policy performance (Section 5.1, Fig. Q1). This is clean, quantitative evidence for a core claim.

- **Zero-shot generalization to unseen abstract language utterances in multi-task settings**: When trained on concrete utterances ("Bring me a tomato," "Bring me an apple") and tested on a semantically related but unseen abstract utterance ("Bring me a fruit"), LGA successfully resolves the ambiguity by constructing an appropriate state abstraction — a capability that GCBC+DART lacks entirely (Section 5.3, Fig. 2B). This directly supports the claim that LMs can "intercede" to handle novel linguistic inputs.

- **Robustness to observational covariate shift**: Policies trained with LGA state abstractions maintain higher success rates than GCBC+DART (a strong baseline designed to mitigate covariate shift via data augmentation) when tested on distributions with novel textures and added distractors (Section 5.2, Fig. 2A). The LGA-L ablation (language-only abstraction) underperforms the full LGA variant, providing evidence that the masked visual input is the critical design choice, not merely the language filtering.

- **Informative ablation isolating design choices**: The contrast between LGA (full masked visual state) and LGA-L (language embedding only) cleanly demonstrates that the instantiation step — converting abstracted features back into visual states — is essential for policy robustness (Section 5.2, Fig. 2A).

- **Real-world pipeline demonstration**: The Spot robot experiments (Section 6) show that the full pipeline (Segment Anything → captioner → LM → policy) can work end-to-end on physical manipulation tasks with household objects, including generalization to novel target objects.

## Weaknesses

### Fatal

None.

### Major

- **No variance reporting or error bars for policy learning results**: Policy performance curves (Figs. Q1, Q2, Q3) are reported as single trajectories with no indication of variance across random seeds, initialization conditions, or test splits. Only 20 test states are sampled per setting, and the paper does not state the number of independent trials. Given that the CNN+MLP policies are trained from scratch, random initialization and data sampling could produce non-trivial variance. The absence of any uncertainty quantification substantially weakens the evidence for sample-efficiency and robustness claims. This is a significant methodological gap for a top-venue paper.

- **Simulation evaluation bypasses the perception bottleneck using ground-truth segmentation**: The textualization step in simulation uses ground-truth segmentation masks and object descriptions from the simulator (lines 166, 176). This means the main experimental results (Q1, Q2, Q3) test the LM feature-selection and policy learning steps under idealized perception, not the full pipeline under realistic conditions. While the paper includes real-world Spot experiments that use actual segmentation/captioning, those are qualitative (single trial per task, no systematic evaluation). The paper's framing emphasizes generality for "unstructured environments," but the hardest part of that claim — reliable perception-to-text conversion — is not evaluated quantitatively.

### Minor

- **No direct measurement of abstraction quality**: The paper evaluates abstraction quality exclusively through downstream policy performance, which conflates two questions: (a) does the LM select the correct features? and (b) does training on masked observations improve learning? The novel claim is (a), yet there is no direct analysis — e.g., precision/recall of the LM's feature selection against ground-truth feature sets. The paper explicitly justifies this choice (lines 185-188), but a direct metric would substantially strengthen the contribution, especially for the Q3 setting where it is unclear whether the LM actually generalized correctly (e.g., selecting both tomato and apple when asked for "fruit").

- **Limited spatial complexity relative to framing**: The evaluation environment uses 4 discretized state locations for objects (line 192), and the abstraction task reduces to identifying relevant object types and colors from a predefined list. The paper's motivation discusses "unstructured environments with many objects, distractors, and possible goals" (line 20) and spatial reasoning challenges, but the experiments never require reasoning about spatial relationships, relational properties, or features beyond simple object attributes. The paper partially acknowledges this in the limitations (line 301), but the gap between framing and evaluation is notable.

- **Missing architectural and training details**: The CNN+MLP policy architecture is described only as "a CNN architecture" and "an MLP" (line 180). Training hyperparameters (learning rate, batch size, optimizer, number of gradient steps, weight initialization) are not reported. This makes the results difficult to reproduce or fully assess.

- **Only one language model tested**: All experiments use GPT-4 (gpt-4-0613). The claim that "LMs" can perform this task would be strengthened by testing a smaller or different model (e.g., Llama, Claude) to understand robustness to LM choice.

### Trivial

- None.

## Nice-to-Haves

- Direct evaluation of LM feature selection accuracy (precision/recall) against ground-truth feature sets would decouple the abstraction claim from the policy learning claim and directly validate the novel component.
- Evaluating the full perception-to-abstraction pipeline in simulation with a real segmentation model (rather than ground-truth) would surface the practical failure modes more convincingly.
- Comparing against a learned representation baseline (e.g., training an encoder with an information bottleneck, or a VAE-based approach) would better position LGA against unsupervised alternatives, though the paper's IL setting makes this non-trivial.

## Removed Points

These points were flagged for removal. Treat them with caution; they may be inaccurate or already addressed.

- *Critic's claim that the Human baseline involved typing features from memory*: The paper explicitly states "we provide the full feature list for easy access" (line 213). The critic misread the setup.
- *Criticism about missing comparison to learned representations (SIRL, beta-VAE)*: The paper cites these as related work but the methods require RL or unsupervised learning setups, not the imitation learning setting evaluated here. This is scope creep — the paper's contribution is about LM-based abstraction, not representation learning.
- *Criticism about LGA-HILL value not demonstrated*: The paper acknowledges comparable performance and justifies LGA-HILL through high-stakes and personalization scenarios. This is not a weakness, just an unsurprising empirical result.
- *Formatting/style nitpicks and complaints about parser-stripped appendix content*: Standard filtering according to review guidelines.

## Novel Insights

None beyond the paper's own contributions. The reviews largely surface the paper's genuine strengths (the human study, zero-shot generalization, robustness results) and identify the main gaps (lack of error bars, bypassed perception bottleneck in simulation, limited spatial complexity). No novel synthesis emerged beyond what the authors themselves articulate.

## Suggestions

1. **Report policy learning results across multiple seeds (at least 5) with error bars or confidence intervals.** This is the single most impactful change. Most of the paper's quantitative claims depend on these curves, and without variance estimates the reader cannot distinguish real improvements from noise.

2. **Add a direct evaluation of LM feature selection quality**, at minimum reporting the feature sets selected for each task and computing precision/recall against the ground-truth feature sets defined by the authors. This would directly validate the novel component of the pipeline.

3. **Test with at least one additional LM** (e.g., a smaller open-weight model) to demonstrate that the approach is not brittle to LM choice.

4. **Provide full architectural and training details** (CNN layer specifications, optimizer, learning rate, batch size, training steps) in the main paper or a public supplement.

5. **Consider running at least one simulation experiment using a real segmentation model** (e.g., SAM + a captioner, as used on the robot) rather than ground-truth simulator state, to quantify the perception gap.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>