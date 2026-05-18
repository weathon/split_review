Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper revisits object hallucinations in LVLMs from an architectural perspective, conducting a diagnostic experiment that attributes the primary source of hallucinations to cross-modal alignment failures rather than visual encoding deficiencies (74.58% of hallucination cases involve correct detection but incorrect inference). Motivated by this finding, the authors propose PATCH, a method that inserts trainable virtual tokens between image features and detection-augmented text prompts to bridge the cross-modal gap with minimal parameter tuning (0.08M parameters). Experiments on POPE and PhD datasets across LLaVA-v1.5, MiniGPT-4, and MiniGPT-v2 show consistent improvements over baselines including HA-DPO, HACL, Woodpecker, and a Hard Prompt baseline.

## Strengths

1. **Novel diagnostic experiment linking hallucinations to cross-modal alignment.** The controlled comparison in Section 2 (Table 1) — where the visual encoder is attached to a detection head and compared against full LVLM inference — provides direct evidence that the visual encoder encodes sufficient object information in the majority of hallucination cases, pointing to a downstream alignment problem. This architectural-level analysis is a genuine contribution beyond the usual data/distribution-level analyses in prior work.

2. **Strong and consistent empirical gains across models.** PATCH achieves substantial improvements over baselines on all three backbones (e.g., +30.46% on MiniGPT-4, +5.03% on LLaVA-v1.5, +6.70% on MiniGPT-v2 on the POPE dataset) while training only 0.08M parameters (0.0012% of total). The gains are consistent and are shown to generalize to the PhD benchmark across five task types.

3. **Systematic ablation studies clarify design choices.** The paper ablates bounding boxes, object categories, token position, token initialization, and token quantity (Tables 3, 4, Figure 2), providing actionable insights into what drives performance. The finding that late placement of virtual tokens reduces accuracy (87.60% vs. 90.03%) and that removing both bboxes and categories drops performance to 82.60% confirms the tokens are genuinely leveraging detection information rather than functioning as generic adapters.

4. **Parameter efficiency and practical flexibility.** PATCH's design — freezing all backbone parameters, training only the token embeddings, and inserting them into the vocabulary at inference — means the method can be applied to any LVLM with minimal compute overhead at training time and can be toggled on/off depending on whether detection information is available.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core methodological contribution and empirical results are sound.

### Minor

1. **The diagnostic claim is slightly over-precise.** The experiment in Section 2 shows that the visual encoder captures sufficient object information (a detection head can extract it), so the hallucination must arise downstream — i.e., from "inadequate decoupling" rather than "insufficient extraction." However, the paper sometimes attributes this specifically to the *projection layer* (line 14: "insufficient cross-modal alignment at the projection layer"), whereas the experiment only rules out the visual encoder. The failure could equally lie in the LLM's inability to interpret the projected features. The broader claim (alignment vs. encoding) is well-supported; the component-level attribution ("projection layer") is not directly tested.

2. **The "state-of-the-art" framing conflates the value of the detection oracle with the value of the virtual token mechanism.** PATCH vs. HA-DPO, HACL, and Woodpecker is an apples-to-oranges comparison: those methods do not have access to external detection information. The paper *does* include the Hard Prompt baseline (which uses the same detection info) and PATCH outperforms it, which partially addresses this. But the paper's language (line 170, "achieving the state-of-the-art performance" grouped with the three non-detection methods) invites the misleading interpretation that the reported gains are solely due to the virtual token design rather than primarily due to the injection of oracle-level detection information. The contribution of the virtual token mechanism beyond simply adding detection info should be more precisely quantified and framed (e.g., on MiniGPT-4, Hard Prompt adds +13.06%; PATCH adds an additional +17.40% — this latter margin is the actual contribution of the method).

3. **No analysis of sensitivity to the object detector.** PATCH is trained and evaluated with the same frozen Cascade Mask R-CNN detector. The virtual tokens may be learning to "translate" the output idiosyncrasies and failure patterns of that specific detector. Whether the method transfers to a different detector (e.g., DINO, YOLOv8) or to a different detection output distribution is unexplored, which limits the practical generalizability claims.

4. **Token initialization effect confounds the interpretation of what the tokens learn.** Accuracy jumps from 86.77% (random initialization) to 90.03% (initialization with a task-tailored prompt). This large gap (3.26%) suggests that much of the gain comes from the prompt-like initialization acting as a soft-prompt prior, rather than from learning a generic cross-modal alignment. The paper should discuss this more candidly — the tokens are effectively doing learned prompt engineering conditioned on the initialization template.

5. **No error bars or variance reported.** Neither the POPE results (Table 2) nor the PhD results (Figure 1) report standard errors, confidence intervals, or multi-seed runs. Given that the PhD test set is only 20% of the data, the differences across task types could be noisy. This is standard practice that should be addressed.

### Trivial

- The "plug-and-play" claim (abstract, Section 3.2) is accurate for the virtual token embeddings being addable/removable from the vocabulary, but the full pipeline still requires running an external detector at inference time. The claim should be slightly tempered or clarified.
- The Hard Prompt baseline is listed alongside HA-DPO, HACL, and Woodpecker as a "hallucination solving method," but it is simply a prompt modification with no training. A clearer distinction would help readers.

## Nice-to-Haves

- **Comparison against a fine-tuned detection-augmented baseline without virtual tokens.** An ablation that fine-tunes the LLM's input embeddings (or a LoRA adapter) on the same detection-augmented training data, without virtual tokens, would more cleanly isolate whether PATCH's architectural choice of virtual tokens matters beyond simply having learnable parameters that process detection information.
- **Analysis of computational overhead.** The added inference-time cost of running the object detector and the latency impact of the additional tokens should be reported.
- **Robustness to detection noise.** An ablation with artificially corrupted detection outputs (e.g., dropped boxes, wrong categories) would show whether the virtual tokens learn to filter noise or propagate errors.
- **Evaluation on additional hallucination benchmarks** (e.g., MME, CHAIR) would strengthen the generalization claim, though the current two-benchmark evaluation is already adequate.

## Removed Points

- **"The paper does not compare against any method that also incorporates detection data"** — This is factually incorrect. The paper explicitly compares against the Hard Prompt baseline (Section 4.2), which concatenates detection categories and bounding boxes as plain text tokens. The paper *does* compare against a method using detection data; the limitation is that Hard Prompt is not fine-tuned, which is a separate issue addressed in Nice-to-Haves above.
- **The claim that "the massive improvements ... are driven almost entirely by the injection of detection info, not by the virtual token design"** — This overstates the case. On MiniGPT-4, Hard Prompt (detection info alone) adds +13.06%, while PATCH (detection info + virtual tokens) adds +30.46%, meaning the virtual tokens contribute an additional +17.40% beyond the detection info. The virtual tokens are clearly doing substantial work beyond simply conveying detection information.
- **"The Hard Prompt baseline is referred to as a hallucination solving method" as a distinct criticism** — This is a presentation preference, not a substantive weakness. The paper clearly describes Hard Prompt as "a simple approach" (Section 4.2) and consistently reports it alongside other comparisons. A relabeling would be trivial.

## Novel Insights

None beyond the paper's own contributions. The diagnostic experiment's finding that 74.58% of hallucination cases involve correct detection but incorrect inference is the most novel insight the paper offers, and the reviewers' analyses do not independently produce additional novel observations about the method or the problem.

## Suggestions

1. **Temper the diagnostic claim** to "downstream of the visual encoder" rather than specifically "at the projection layer," or add an experiment (e.g., probing the projected features) to support the component-level attribution.
2. **Reframe the SOTA comparisons** by clearly separating methods with and without external detection information, and explicitly quantifying the marginal benefit of the virtual tokens over and above the detection information itself.
3. **Add detector robustness experiments** — even a single alternative detector (e.g., DINO, YOLOv8) would substantially strengthen the generalizability claim.
4. **Report confidence intervals or standard deviations** for all main results, particularly the PhD dataset where sample sizes per task type may be small.
5. **Discuss the initialization sensitivity** more candidly — acknowledge that the 3.26% gap between random and prompt-based initialization indicates a significant prompt-engineering component in the token learning.

## Score and Decision

The paper makes a genuine contribution with its diagnostic analysis and the PATCH method, which is parameter-efficient, empirically effective, and evaluated across multiple backbone models and benchmarks. The weaknesses are not fatal: the diagnostic claim is slightly over-precise but directionally correct, and the SOTA framing is somewhat misleading but not dishonest given that Hard Prompt is included. These issues can be addressed in a revision.

**Originality:** Good — the diagnostic perspective is novel. **Importance:** High — hallucination mitigation is a central challenge. **Claims supported:** Mostly — the method works as advertised; the causal claim is modestly over-claimed. **Soundness:** Good — experiments are well-designed, though missing variance reporting and detector sensitivity analysis. **Clarity:** Good. **Value to community:** High — the method is practical and the diagnostic insights are actionable.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>