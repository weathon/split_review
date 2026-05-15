Now I have all the information I need. Let me write the consolidated review.

---

## Summary

The paper proposes COGT (Causally-Ordered Generative Training), which uses an off-the-shelf dependency parser to build a Causal Graphical Model (CGM) from captions. This CGM defines a partial order for token prediction in a generative decoder: tokens are predicted following the level-order traversal of the dependency tree, conditioning only on their ancestors. The decoder is trained on top of a frozen VLM encoder (CLIP, XVLM, InstructBLIP) and used at inference to score candidate captions via the CGM-structured likelihood. Experiments on five compositional benchmarks show that COGT substantially outperforms prior compositional methods and standard autoregressive/parallel generative strategies.

## Strengths

- **Novel and well-motivated approach**: Using syntactic dependency trees to guide token prediction order in a generative decoder for compositionality is elegant, underexplored, and principled. The paper clearly motivates why predicting "brown" after knowing "bird" (its head) reduces ambiguity compared to standard left-to-right AR. The resulting semi-parallel generation that respects the tree's level order is a natural fit.

- **Strong controlled ablation (Table 1)**: The paper compares COGT's CGM-guided ordering against Sequential-AR, Fully-Parallel, and Mixed under the same decoder architecture and frozen CLIP encoder. COGT achieves an average improvement of +17.77 points over Fully-Parallel and substantially beats Sequential-AR and Mixed. This isolates the core contribution of the CGM ordering, independent of the decoder architecture.

- **Consistent SOTA across multiple VLMs and benchmarks**: COGT applied to CLIP, XVLM, and InstructBLIP sets new SOTA on ARO, SugarCrepe, VL-CheckList, ColorSwap, and FG-OVD. COGT-CLIP trained on only COCO (~100K images) outperforms DAC-LLM trained on CC3M (~3.3M images) by 12.27 points average (Table 3). COGT-XVLM+ outperforms Cap and CapPa (pre-trained on 1B image-text pairs) despite using far less pre-training data (Table 5).

- **Thorough ablations validate design decisions (Table 2)**: The paper systematically ablates parser quality (Deep Biaffine+RoBERTa best), mask-specific tokens (+2.69 points), and two-layer visual features (+4.75 points), confirming each component contributes measurable value.

- **No degradation on standard downstream tasks (Table 6)**: COGT does not harm (and slightly improves) linear probing accuracy on CIFAR10/100 and ImageNet, mitigating a known problem with many compositional fine-tuning methods.

- **Method is robust across parser quality**: Even with the weaker Deep Biaffine parser, COGT outperforms all prior methods in Table 3 (best previous DAC-LLM: 76.08 vs. COGT with weak parser: 86.77 average), showing the approach does not depend on a perfect parser.

## Weaknesses

### Fatal
None.

### Major

- **"Causal" framing is overstated**: The paper repeatedly uses "causal dependencies," "causally sufficient," and "discarding spurious associations" (Sections 1, 3, conclusion) to describe what is ultimately a syntactic ordering heuristic. The method does not perform causal inference (no interventions, do-calculus, or counterfactual reasoning). The dependency tree provides a linguistically-motivated partial order for token prediction, and the paper shows this ordering is empirically beneficial — but this does not validate the causal interpretation. The paper partially acknowledges this ("we interpret the dependency relations... as causal relations because they directly model the linguistic influence") but the title ("Causal Graphical Models") and the pervasive causal language suggest a stronger theoretical grounding than is demonstrated. This does not invalidate the method, but it is misleading and should be toned down.

- **Headline claim conflates architecture and ordering contributions**: The abstract and conclusion claim COGT "largely outperforms all the state-of-the-art compositional approaches." While the results in Tables 3–5 support this, the comparison mixes two factors: (a) the CGM ordering and (b) the addition of a generative decoder to an encoder-only backbone (e.g., CLIP). The ablation (Table 1) correctly isolates the CGM ordering by comparing against Sequential-AR under the same architecture, but this controlled comparison is not repeated in the main comparative tables (3–5), where the baselines include encoder-only fine-tuning methods. The paper would be stronger if it either included the Sequential-AR/Parallel baselines in the main tables or more carefully framed the claim as "the full COGT system (generative decoder + CGM ordering) outperforms prior methods, with ablations showing the CGM ordering itself is responsible for a significant portion of the gain."

### Minor

- **No error bars or variance reported**: None of the experiments report standard deviations, confidence intervals, or number of seeds. Given the stochastic nature of parser outputs and decoder training, some measure of variance is expected for a paper making SOTA claims. This is standard practice for empirical work and should be addressed.

- **Parser error sensitivity is not analyzed**: The paper tests three parsers (Table 2) and shows that better parsers yield better results, but does not analyze what happens when the parser makes errors — e.g., how often it misassigns dependency relations, and how parse errors affect the likelihood ranking at inference. A manual error analysis on a sample of captions (e.g., 200 instances) comparing accuracy on correct vs. incorrect parses would substantially strengthen the paper.

- **Limited domain generalization evidence**: Training is on COCO (and in the + variants, COCO+CC3M+VG), and most test benchmarks are derived from COCO images/captions. While the paper acknowledges removing overlapping VG data, it does not include an evaluation on a substantially different domain. The CC3M data provides some diversity (web-crawled Alt-text), but a dedicated out-of-distribution experiment would strengthen claims about generalization.

- **Missing "random parent" baseline**: The paper compares full dependency tree ordering vs. sequential/parallel baselines, but does not test whether the specific linguistic structure matters versus *any* tree structure. A control where a random tree (same number of nodes, random edges) replaces the dependency parser would verify that the linguistic parse, not just any structured ordering, is responsible for the gains.

### Trivial
None.

## Nice-to-Haves

- Include a few qualitative case studies showing concrete examples where COGT's likelihood ranking corrects errors made by Sequential-AR or Fully-Parallel, with visualizations of the dependency tree. This would help readers build intuition for how the CGM ordering helps.
- Report Winoground results (the paper states these are in App. C.2, which was stripped by the parser).
- Add Sequential-AR/Fully-Parallel baselines to the main comparison tables (3–5) for readers who might skip the ablation section.

## Removed Points

These points from the harsh review were removed or relocated for the reasons stated below; treat them with caution:

1. **"Winoground is excluded with a weak excuse"** — The paper states that Winoground results are in App. C.2 (stripped by the parser). The justification (CLIP struggles with out-of-focus objects) is reasonable and many CLIP-based works do skip Winoground for this reason. The paper does not "exclude" it; it is in the appendix.
2. **"The paper never isolates what the CGM ordering buys beyond simply attaching any generative decoder"** — Table 1 provides exactly this control, comparing COGT to Sequential-AR, Fully-Parallel, and Mixed under the same decoder architecture and frozen encoder. The criticism is about presentation (these baselines are not in Tables 3–5), not about missing evidence.
3. **Criticism that FG-OVD "also uses COCO-derived bounding boxes" as a weakness about domain overlap** — The paper proposes FG-OVD as a *new* benchmark; using COCO-derived boxes is appropriate for its purpose of evaluating fine-grained object property discrimination. This is not a weakness of COGT itself.
4. **"The paper does not test whether the claimed removal of 'spurious correlations' actually happens"** — While true that no direct test of spurious correlation removal is performed, the empirical improvement over baselines is indirect but reasonable evidence. This is a stringent theoretical demand for an empirical systems paper.
5. **Several generic "strengths" from the Strength Finder that conflict with verified weaknesses or are generic (e.g., "method is simple" — retained; but "addresses an important problem" is dropped as generic and unspecific).**

## Novel Insights

The most interesting finding from the reviews is the robust performance of COGT even with weaker parsers. Table 2 shows that the worst parser (Deep Biaffine, 86.77 average) still outperforms all prior methods in Table 3 (best previous, DAC-LLM: 76.08). This suggests that the dependency tree structure provides a useful inductive bias that is relatively robust to parser quality — the method is not brittle. This is a genuine strength of the approach that deserves more emphasis in the paper, as it addresses a natural concern about dependency on parser accuracy. Another notable angle is that COGT-CLIP trained only on COCO (~100K images) beats methods trained on CC3M (~3.3M), suggesting that the CGM-guided factorization makes more efficient use of training data — a claim the paper makes but does not rigorously support with a data-scarce experiment.

## Suggestions

1. **Reframe the causal language**: Change the title or at minimum the presentation to replace "causal" with "dependency-structured" or "syntactically-guided." The method is strongest as a practical, empirically-validated ordering heuristic, not as a causal model. The paper should acknowledge that while the CGM formalism is used to define the factorization, the actual contribution is a linguistically-structured prediction order, not causal discovery or intervention.

2. **Add a "random tree" control**: Include a baseline where the dependency parser is replaced by a randomly generated tree over the same tokens (same number of nodes, random parent assignments). If COGT significantly outperforms this baseline, it directly demonstrates that the specific linguistic dependencies are the source of improvement, not just any structured ordering. This is a simple experiment that would substantially strengthen the paper.

3. **Report variance**: Add standard deviations over at least 3 seeds for the key comparisons in Tables 1 and the main result (COGT-CLIP vs. baselines). This is standard practice.

4. **Include Sequential-AR in main tables**: Add the Sequential-AR baseline (which is already a generative decoder with standard AR ordering) to Tables 3–5 so readers can directly see the improvement attributable to the CGM ordering alongside the comparison to prior methods.

5. **Manually analyze parser errors**: On a sample of ~100–200 test captions, label whether the dependency parser produced a correct parse, then compare COGT's accuracy on correctly-parsed vs. incorrectly-parsed captions. This would directly address the parser robustness concern.

---

## Score and Decision

The paper presents a genuinely novel and well-motivated idea, supported by strong controlled ablations and SOTA results across five benchmarks and three backbone VLMs. The main weaknesses — overstated causal framing, absence of error bars, and insufficient parser error analysis — are presentation and rigor gaps rather than fatal methodological flaws. None of the identified weaknesses undermine the core empirical finding that CGM-guided ordering substantially improves compositional understanding over AR, parallel, and mixed strategies, and that the full COGT system outperforms prior methods by large margins. With reasonable revisions, particularly toning down the causal claims and adding variance reporting, this would be a strong contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>