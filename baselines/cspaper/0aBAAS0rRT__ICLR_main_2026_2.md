---
job_id: 4860dea2-3ab6-42bd-87b5-3c6800279ccf
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0aBAAS0rRT.pdf
paper: Map as a Prompt: Learning Multi-Modal Spatial-Signal Foundation Models for Cross-Scenario Wireless Localization
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centering on self-supervised representation learning, transfer/generalization across environments, multimodal conditioning, and graph-based modeling for wireless localization.

## Minimum Quality
Pass ✅. The paper contains the essential components needed for scientific review, including abstract, introduction with prior-work discussion, methodology, experiments with quantitative results, and conclusion; while there are important clarity and rigor issues, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-targeting text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes SigMap, a two-stage wireless localization model that first pre-trains a transformer backbone on CSI data using a cycle-adaptive masked modeling objective, then fine-tunes it with a geographic “map-as-prompt” mechanism derived from 3D scene graphs. The method combines signal-side self-supervision with map-conditioned prompt tuning, and is evaluated on DeepMIMO and WAIR-D for single-BS, multi-BS, and cross-scenario localization.

## Strengths
The paper targets an important problem. Cross-scenario wireless localization with limited labels is genuinely hard, and the attempt to combine CSI pretraining with environmental conditioning is timely and relevant to the ICLR community.

The overall idea is interesting: use masked modeling to learn signal representations, then adapt with lightweight map prompts instead of fully retraining the model. This is a reasonable and practically motivated design choice, especially for scenario transfer.

The empirical results are directionally strong. In **Table 1** on single-BS localization, the gap between SIGMAP (w/ map) and the strongest listed baseline is substantial in MAE and especially in CDF@1m. Likewise, **Table 2** shows consistently better multi-BS performance, and the gains over both classical OMP and learned baselines suggest that the proposed combination of pretraining plus geographic conditioning is useful, at least under the tested settings.

The paper includes useful component analyses rather than only headline numbers. **Table 3** directly tests the masking strategy, and **Table 4** tests different map modalities, which is the right instinct for a paper making two main methodological claims.

Some figures help communicate the method. **Figure 2** gives a reasonably intuitive view of the two-stage pipeline and makes the separation between pretraining and prompt-based fine-tuning easy to follow. **Figure 4** is also useful in showing how the geographic prompt is generated from a graph over building vertices and BS locations; that is one of the more concrete parts of the paper’s multimodal story.

The parameter-efficiency angle is a real strength. Even though I have questions about exact accounting, the idea of freezing the backbone and adapting only prompt-generation and task heads is appealing for deployment across new environments.

## Weaknesses
1. **The paper over-claims “foundation model” status relative to the actual training setup and evidence.**  
   The central training data described in **Section 4.1** and **Appendix B.3** is essentially one primary pretraining scenario, DeepMIMO O1_3p5, with multiple frequency settings but the same environment family. That is not strong evidence for a broad “foundation model” in the sense commonly expected by the community. What is actually shown is a pretrain-then-adapt localization model with some transfer ability, which is still worthwhile, but materially narrower than the title and several claims suggest. This matters because the paper’s contribution is positioned at a much broader level than what the empirical evidence supports. The generalization section in **Page 9-10** is better described as few-shot cross-scenario adaptation than zero-shot or foundation-scale generality.

2. **There are multiple inconsistencies and underspecified details in the mathematical formulation, especially around the input representation and training objective.**  
   On **Page 5, Equation (5)**, the CSI is represented as $\mathbf{X} = [\Re(\mathcal{H}), \Im(\mathcal{H})]$. But in **Appendix B.2, Equation (12)**, the input is instead described as magnitude and phase, $\overline{\mathbf{H}}_s = [|\mathbf{H}_s|, \angle \mathbf{H}_s]$. These are not equivalent parameterizations for learning behavior, especially under masking and reconstruction. The main paper should clearly specify which representation is actually used in all experiments. This is not a cosmetic detail, because periodicity detection, masking structure, and reconstruction difficulty can differ markedly between real/imaginary and magnitude/phase views.  
   There is a second issue: **Equation (7)** defines the MAE loss as a full reconstruction error $\mathbb{E}\| \mathbf{X} - f_{\theta_{\text{des}}}(\mathbf{X}_{\text{masked}})\|^2$, but masked autoencoding is normally evaluated either only on masked positions or with explicit weighting. If the loss is computed over all positions, the paper should explain how trivial copying of visible entries is prevented from dominating optimization. The masking ratio, visible-token handling, and whether the loss is restricted to masked entries are all omitted from the main paper. These missing pieces directly affect whether the self-supervised objective is well-defined and whether the claimed benefits of the masking strategy are scientifically interpretable.

3. **The cycle-adaptive masking mechanism is not specified tightly enough in the main paper to be fully assessable, and its core variables are underdefined.**  
   In **Equation (6)** on **Page 5**, the mask is defined using $d_{\text{final}}$, $j_0$, and $w$, but the procedure that derives $d_{\text{final}}$ from cross-correlation is not provided in the main text. The paper says it computes “row-wise cross-correlation and generating shift-aware patterns,” but there is no precise algorithmic definition in the main paper for how the dominant shift is selected, how ties are resolved, whether shifts are per-sample or per-batch, or how robustness is handled when periodicity is weak or noisy. The appendix gives more intuition, but the main-paper method is still too hand-wavy for a central contribution.  
   Relatedly, **Figure 3** visually suggests adaptive diagonal masks based on periodic stripes in the CSI amplitude. The figure is helpful qualitatively, but it also exposes the current weakness: the method depends on detecting a clean periodic shift structure that may not hold across all CSI regimes. The paper does not quantify how often such a dominant shift exists, nor whether the masking strategy degrades when the heatmap resembles the $d=0$ or weak-structure cases shown later in **Figure 7**.

4. **The geographic prompt formulation is conceptually interesting, but the graph construction and prompt integration are too shallowly justified.**  
   In **Section 3.4** and **Algorithm 1** on **Page 6**, the graph is built from building vertices plus BS positions, with edges from Delaunay triangulation. This is a plausible engineering choice, but the paper never explains why Delaunay adjacency is the right inductive bias for propagation-aware reasoning. Wireless propagation depends on occlusion, material interaction, visibility, path length, and reflection geometry, none of which are explicitly represented by a vanilla triangulation graph over vertices. As written, the map prompt seems to compress a potentially very rich 3D environment into a global mean pooled graph embedding, which risks discarding exactly the local geometric structure that should matter most for localization.  
   **Figure 4** clearly shows this compression pipeline, from coordinates to triangulation to two GCN layers to global mean pooling to a single prompt token. Ironically, the figure makes the limitation easier to see: a whole scene is reduced to one pooled vector before being prepended as a single token. That could work empirically, but the paper does not test whether one prompt token is enough, whether local prompts are better, or whether the graph features capture any propagation-relevant semantics beyond coarse geometry.

5. **Equation-level inconsistencies and notation problems reduce confidence in the technical presentation.**  
   The GCN update is given on **Page 6** as
   $$
   \mathbf{H}^{(l+1)} = \sigma\left(\tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}\mathbf{H}^{(l)}\mathbf{W}^{(l)}\right),
   $$
   but **Algorithm 1, line 7** uses a different message-passing form
   $$
   \mathbf{h}_i^{(l)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{h}_i^{(l-1)} + \sum_{j\in\mathcal{N}(i)} \mathbf{U}^{(l)}\mathbf{h}_j^{(l-1)}\right).
   $$
   These are not identical formulations unless additional normalization or parameter tying is specified. The paper presents both as if they are interchangeable.  
   There is also a likely typo or broken expression in the final forward-pass definition on **Page 7**:
   $$
   f(\mathbf{X},\mathcal{M},\mathbf{P}_{\text{BS}})=f_{\theta_{\text{task}}}(f_{\theta_{\text{tau}}}([\mathbf{T}_{\text{geo}};\mathbf{T}_{\text{CSI}}])),
   $$
   where the notation appears malformed in the manuscript. This is precisely the kind of equation that should be clean, because it defines what is trainable during adaptation.  
   More seriously, **Equation (11)** on **Page 8**, the claimed “NLoS-aware attention mechanism,” appears nowhere in the earlier methodology. The variables $\boldsymbol{o}_s^{(i)}$, $\phi(\cdot)$, and $\mathbf{W}_{\mathrm{NLoS}}$ are undefined in the method section, and there is no explanation of how this equation connects to the actual multi-BS attention in **Equations (9)-(10)**. This reads like a post hoc justification rather than a properly integrated method. That is a major issue, not a small typo.

6. **The experimental comparisons are not as strong as the “state-of-the-art” framing suggests.**  
   The baseline set in **Section 4.2** is fairly limited: OMP, CNN, SWiT, and LWLM. Given the paper’s claims about multimodal learning, map conditioning, and foundation-model-style transfer, the evaluation should do more to compare against stronger or more directly relevant map-aware and multimodal baselines. The paper cites prior work on map-assisted localization in the introduction, but there is no direct empirical comparison to a map-assisted deep model beyond the paper’s own ablations. The literature positioning also misses several relevant threads on geographic databases / 3D scene generation for RF modeling and multimodal wireless foundation models. This matters because a strong relative result against a narrow baseline set is not the same as a convincing state-of-the-art result.  
   Concretely, **Table 1** and **Table 2** show good gains, but since the baseline pool is limited, it remains unclear whether the gains come from the self-supervised backbone, the prompting mechanism, simply adding map information, or implementation differences against somewhat dated baselines.

7. **The ablations are helpful but still incomplete for isolating causality.**  
   **Table 3** compares masking variants, but the results are slightly awkward: adaptive masking has the best MAE and CDF@1m, while strip masking has a better RMSE than adaptive masking ($0.972$ vs $1.099$). The paper does not discuss this inconsistency. If adaptive masking is the clear winner, why does it lose on RMSE? Is it reducing median-type errors while increasing a tail of outliers, or vice versa? The omission matters because the paper’s story is “better trade-off,” yet the trade-off is not analyzed.  
   Similarly, **Table 4** evaluates 3D vs 2D map prompts, but there is no ablation on prompt token count, GNN depth, graph construction choice, frozen-vs-unfrozen backbone, or how much performance comes from map prompts alone without SSL pretraining. A paper with two main ingredients should more systematically test interactions: no-pretrain + map, pretrain + no-map, pretrain + map, full fine-tuning + map, etc.

8. **The “zero-shot generalization” claim in the abstract is not supported by the actual protocol described in the experiments.**  
   On **Page 9**, the paper explicitly states that on unseen scenarios, “only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario).” That is few-shot adaptation, not zero-shot. The abstract and some broader claims should be corrected. This is not just wording nitpicking, because zero-shot and few-shot are different scientific claims about transfer. Overstating this point weakens trust in the presentation.

9. **The practical assumptions around map availability and deployment are under-discussed.**  
   The method relies on 3D environment maps and BS positions at inference time. For some settings this is plausible, but for others it is a substantial assumption. The paper briefly tests 2D bird’s-eye prompts in **Table 4**, which is useful, but it still does not discuss what happens when maps are incomplete, noisy, outdated, or misaligned with the ray-tracing coordinate frame. Since the proposed benefit is cross-scenario adaptation, robustness to imperfect geographic information is an important practical dimension. Without it, the current results are somewhat idealized.

10. **There are several presentation and consistency issues in the results section that, while individually small, accumulate and make the paper feel less polished than it should be.**  
   The paper says “Results are listed in Table 4.5” on **Page 9**, but there is no properly numbered table there. On **Page 10**, the text reports “1.580 m on WAIR-D Scenario-2,” while the table immediately above lists **1.880 m** for SIGMAP (w/ map). Appendix B.3 gives the train/val/test split as “10,000/1,000/10,00,” which is likely a typo. **Figure 5** is a radar chart summarizing performance across scenarios/metrics, but it is not especially informative because it mixes heterogeneous metrics and conditions into one normalized-looking visualization without clear scale interpretation. The figure looks nice, but scientifically the tables are doing the real work here.

## Questions
1. Please clarify the actual CSI representation used in all experiments. Is the model trained on $\left[\Re(\mathcal{H}), \Im(\mathcal{H})\right]$ as in **Equation (5)**, or on $\left[|\mathcal{H}|, \angle\mathcal{H}\right]$ as in **Equation (12)**? If the choice differs between pretraining and fine-tuning, please say so explicitly and explain why.

2. For the masked reconstruction loss in **Equation (7)**, is the loss computed over all entries or only masked entries? Please provide the exact objective, including mask ratio, tokenization scheme, and whether visible entries contribute to the loss.

3. How exactly is $d_{\text{final}}$ in **Equation (6)** computed from cross-correlation? A precise algorithm in the rebuttal would materially increase confidence. In particular, is the shift estimated per sample, per antenna row, or globally, and how stable is it when periodicity is weak?

4. What is the relationship between the multi-BS attention in **Equations (9)-(10)** and the “NLoS-aware attention” of **Equation (11)**? Right now they look like different mechanisms. Is Equation (11) actually used in experiments? If yes, it needs to be integrated into the method section and fully defined.

5. Can the authors provide a cleaner factorized ablation isolating the contribution of:  
   (a) self-supervised pretraining,  
   (b) cycle-adaptive masking,  
   (c) map prompting,  
   (d) parameter-efficient freezing versus full fine-tuning?  
   This would help determine whether the main gains are architectural, data-modal, or optimization-related.

6. For **Table 3**, why does adaptive masking improve MAE and CDF@1m but not RMSE relative to strip masking? Some discussion of the error distribution, perhaps with percentile statistics or CDF plots for the ablations, would strengthen the claim.

7. Please temper or justify the “zero-shot” terminology. If target-scenario task heads are fine-tuned on about 100 samples, the current protocol appears few-shot rather than zero-shot.

8. How sensitive is the map prompt to map noise or geometric simplification beyond the 2D/3D comparison in **Table 4**? For example, what happens with perturbed building vertices, missing buildings, or coordinate misalignment? Even a small robustness study would make the deployment story more credible.

9. Why was Delaunay triangulation chosen for graph construction in **Section 3.4** instead of a propagation-aware graph, visibility graph, or distance-threshold graph? A stronger justification, or a small comparison, would help.

10. If the authors want to keep the “foundation model” framing, they should explain what definition they are using and why pretraining on the current scale of environments and tasks is sufficient for that terminology.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission itself. The work relies on simulated and benchmark wireless datasets and does not appear to involve human subjects or sensitive personal data in the presented experiments.

## Soundness Rating
2: fair. The empirical results are promising, but several central claims are weakened by under-specified objectives, inconsistent equations, limited baseline coverage, and a mismatch between some claimed and evaluated settings.

## Presentation Rating
2: fair. The high-level story is understandable and some figures are helpful, but the paper has too many notation inconsistencies, typos, undefined variables, and claim/experiment mismatches for me to call the presentation good.

## Contribution Rating
2: fair. The combination of cycle-adaptive masking and map prompting is interesting and potentially useful, but the paper overstates the breadth of the contribution, and the evidence does not fully support the strongest novelty and generality claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a solid core idea and encouraging empirical results, but in its current form the technical specification and experimental substantiation are not quite tight enough for a confident positive recommendation.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main mathematical formulations and experimental claims carefully, though some missing implementation details limit full verification.