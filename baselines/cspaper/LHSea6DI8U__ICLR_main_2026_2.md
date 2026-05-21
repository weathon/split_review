---
job_id: 6727b76a-7afe-4e66-840b-d17de2d3d8e3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: LHSea6DI8U.pdf
paper: A General Spatio-Temporal Backbone with Scalable Contextual Pattern Bank for Urban Continual Forecasting
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it addresses continual learning, learning on graphs, spatio-temporal representation learning, and scalable neural architectures for dynamic forecasting.

## Minimum Quality
Pass ✅. The submission contains the expected components, namely abstract, introduction, related work, methodology, experiments, quantitative/qualitative results, and conclusion, and it presents a complete empirical study. There are technical and clarity issues, especially around the attention formulation and evaluation protocol, but they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes STBP, a continual spatio-temporal forecasting framework composed of a frozen general backbone and an incrementally expanded contextual pattern bank. The backbone combines a frequency-domain temporal module with a dual-stream linear graph attention module, while the pattern bank is updated across periods to adapt to node expansion and distribution shift without retraining the full model. Experiments on three streaming datasets in traffic and air-quality forecasting compare STBP against conventional spatio-temporal models and continual forecasting baselines, with additional few-shot, ablation, case-study, and efficiency analyses.

## Strengths
The paper tackles an important and realistic problem. Continual spatio-temporal forecasting with graph expansion is much closer to deployment conditions than the standard fixed-topology offline setting, and the paper is well motivated in Section 1 and by the setup in Section 5.

The decomposition into a stable backbone plus an expandable contextual pattern bank is a sensible design choice for continual learning. Freezing the backbone after the first stage and adapting only the pattern bank is a clean operational idea, and it gives the method a clear systems interpretation: preserve general knowledge in the backbone, encode scenario-specific adaptation in a lightweight evolving component.

The empirical results are broadly strong. In **Table 1** on Page 7, STBP consistently outperforms the listed baselines across almost all reported datasets, horizons, and metrics. The gains on PEMS-Stream and CA-Stream are not marginal; for example, on PEMS-Stream average MAE, STBP reports \(12.31\) versus \(15.67\) for EAC and \(16.86\) for PECPM, and on CA-Stream average MAE it reports \(15.77\) versus \(20.20\) for EAC. Even on AIR-Stream, where the gap is smaller, STBP remains competitive or best on most average metrics. This consistency matters more than cherry-picked wins on a single horizon.

The ablation and efficiency sections are useful, at least directionally. **Figure 4** on Page 8 indicates that removing the contextual pattern bank, the backbone, or DLGA all degrades performance, which is aligned with the claimed contribution that both the backbone and pattern bank are needed. **Figure 8** on Page 10 also supports the practical scalability claim: STBP sits in a favorable region of the accuracy-time-memory tradeoff compared with several baselines, and the toy scaling plot gives some evidence that the linear-attention variant is cheaper than the quadratic alternative.

The qualitative visualizations help interpret what the pattern bank is supposed to do. **Figure 3** on Page 4 and **Figure 6** on Page 9 show clustered embeddings and evolution of the pattern bank over time, and the node-level forecasting plots in **Figure 7** suggest that STBP tracks local dynamics better than EAC in the selected examples. These figures do not prove the mechanism, but they do make the proposed intuition more concrete.

The paper is reasonably comprehensive experimentally. Beyond the main benchmark in Table 1, the few-shot results in **Table 2** are a useful stress test, and the period-wise breakdowns in Tables 7 and 8, although in the appendix, suggest the improvement is not confined to a single period.

## Weaknesses
1. **The core attention formulation in Equations (8) and (9) is mathematically underspecified and arguably inconsistent with standard linear-attention practice.**  
   On Page 6, the paper first defines
   \[
   \mathbf{H}^{s'}_{\tau}=\mathrm{Softmax}(\mathbf{Q}\mathbf{K}^{\top}+\mathbf{Q}(\mathbf{P}^{(2)}_{\tau})^{\top})\mathbf{V} \tag{8}
   \]
   and then states the approximation
   \[
   \mathrm{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V},\mathbf{P}^{(2)}_{\tau})
   \approx \phi(\mathbf{Q})\left(\phi(\mathbf{K})^{\top}\mathbf{V}+\phi(\mathbf{P}^{(2)}_{\tau})^{\top}\mathbf{V}\right). \tag{9}
   \]
   This is not a faithful linearization of softmax attention as written. Standard linear attention requires a normalization term in the denominator, typically something like
   \[
   \frac{\phi(\mathbf{Q})\left(\phi(\mathbf{K})^\top \mathbf{V}\right)}
   {\phi(\mathbf{Q})\left(\phi(\mathbf{K})^\top \mathbf{1}\right)},
   \]
   possibly with causal or masking variants. Equation (9) drops normalization entirely, which changes the operator substantially. The appendix derivation in Equation (10) does include denominators, but Equation (9) in the main text omits them, and the sentence “with Softmax used for approximation in our implementation” is confusing because softmax is not a random feature map \(\phi(\cdot)\). This matters because DLGA is one of the paper’s central algorithmic contributions. If the main equation is inaccurate, readers cannot tell what model was actually implemented, nor whether the claimed \(O(N)\) complexity is correct for the implemented version.

2. **Equation (4) and the surrounding description of pattern-bank expansion are dimensionally confusing and likely contain notation errors.**  
   On Page 4, the paper writes
   \[
   \mathbf{P}_{\tau}^{\prime} = \mathbf{P}_{\tau - 1} \| \Delta \mathbf{P}_{\tau}, \tag{4}
   \]
   but then on Page 5 states “\(\mathbf{P}_{\tau}\in\mathbb{R}^{(N_{\tau}-N_{\tau-1})\times d}\) represents newly introduced parameters,” which appears to mean \(\Delta \mathbf{P}_{\tau}\), not \(\mathbf{P}_{\tau}\). This is not just cosmetic. The method relies on precise distinctions among \(\mathbf{P}_{\tau}\), \(\mathbf{P}'_{\tau}\), and \(\Delta \mathbf{P}_{\tau}\), and later further splits \(\mathbf{P}_{\tau}\) into \(\mathbf{P}_{\tau}^{(0)}, \mathbf{P}_{\tau}^{(1)}, \mathbf{P}_{\tau}^{(2)}\). The indexing and object identities are muddy enough that I had to reconstruct the intended parameterization myself. For a continual-learning method with expansion, sloppy notation on what is inherited, what is appended, and what is fine-tuned directly affects reproducibility.

3. **The paper makes a strong stability argument for freezing the backbone, but the empirical evidence is not sufficient to show that this design choice is the right tradeoff rather than simply one workable choice.**  
   The central philosophy, introduced in Section 4.1 and used throughout, is that after the initial period the backbone should remain frozen while the pattern bank adapts. This is plausible, but the paper does not convincingly isolate whether freezing is actually preferable to partial backbone adaptation, low-rank adaptation, selective layer unfreezing, or a smaller learning rate on the backbone. The “Online” ablation in Section 5.3 is too coarse because it retrains the full model end-to-end, changing both optimization dynamics and parameter count. A much more informative experiment would compare: frozen backbone + pattern bank, last-layer unfreezing + pattern bank, and all-layer fine-tuning + pattern bank under matched budgets. Without that, the paper’s main continual-learning prescription feels somewhat asserted rather than demonstrated.

4. **The evaluation protocol for non-continual baselines is not entirely fair, and this inflates uncertainty around the size of the gains.**  
   Section 5.2 says GWNet and STID are retrained from scratch at each stage using only current-period data, while iTransformer is trained online on the full current graph initialized from previous weights. These are not symmetric adaptations. More importantly, they are also not the strongest obvious continual variants of those backbones. A stronger comparison would adapt a general backbone with the same continual recipe as STBP but without the proposed pattern-bank mechanisms, or at least compare against a frozen-backbone prompt-free variant under the same data stream assumptions. The paper does include “Online” and “Retrain” in **Figure 4**, which helps, but these are ablations of the proposed model, not independently tuned baselines from the literature. Given how large the margins are in **Table 1**, I would like stronger assurance that some of the gain is not coming from baseline adaptation choices that are weaker than necessary.

5. **The claims around distribution-shift robustness are plausible but not directly validated in the main paper.**  
   A major motivation, repeated in the abstract, introduction, and Section 4.3, is that frequency-domain modeling mitigates distributional drift by extracting stable low-frequency components. However, the main paper does not actually show drift-specific diagnostics or a controlled experiment where drift severity varies and FreNet’s contribution can be isolated. The strongest direct evidence is relegated to the appendix via MMD statistics in Table 6, and even there the table only characterizes the datasets, not the model’s robustness. The ablation in **Figure 4** compares “w/o Backbone” and “w/o DLGA,” but it does not isolate FreNet itself. Since the frequency-domain argument is one of the paper’s main conceptual hooks, it deserves a dedicated ablation in the main paper, not just a broad architectural removal.

6. **Some of the interpretability claims around the contextual pattern bank are overstated relative to the evidence.**  
   The paper repeatedly claims that the pattern bank “distinguishes relevance and heterogeneity,” and **Figure 3** on Page 4 plus **Figure 6** on Page 9 are offered as support. But these are t-SNE visualizations of learned embeddings combined with a few time-series examples. t-SNE can produce visually attractive clusters even when global structure is weak, and the figures do not quantify cluster quality, temporal consistency, or correlation with external node attributes. I do not object to including the plots, but the text goes beyond what they support. A more careful claim would be that the learned pattern bank appears to encode meaningful node structure, not that it clearly disentangles relevance and heterogeneity.

7. **The presentation is uneven, especially where the paper needs to be most precise.**  
   There are several writing issues that make the technical core harder to audit than it should be: the broken line “dynamic struc tural expansion” on Page 2, the inconsistent use of symbols such as \(\mathbf{H}_{\tau}\), \(\mathbf{H}_{\tau}^{f}\), \(\mathbf{H}^{s}_{\tau}\), \(\mathbf{H}^{s'}_{\tau}\), and \(\mathbf{H}'_{\tau}\), and the vague phrase on Page 6 that “Softmax [is] used for approximation in our implementation.” **Figure 2** is visually helpful at a high level, but it also tries to pack too much into one composite illustration. For example, the relation between the three pattern-bank components \(\mathbf{P}^{(0)}, \mathbf{P}^{(1)}, \mathbf{P}^{(2)}\) and the exact insertion points into FreNet and DLGA is only partially clear from the figure and still requires deciphering the text. This affects the paper’s scientific value because the method is not simple enough that implementation details can be safely hand-waved.

8. **The efficiency claim is directionally supported, but the evidence is thinner than the paper suggests.**  
   In **Figure 8** on Page 10, the efficiency comparison is only reported on PEMS-Stream and AIR-Stream, not on the most dramatic topology-growth scenario CA-Stream, where scalability is arguably most important. The toy scaling plot is useful, but toy scaling plus two real datasets is not yet a complete efficiency story. Also, the plot mixes training time and memory in a qualitative scatter format without reporting exact values or variance, which makes it harder to judge whether the “minimal overhead” claim is robust. Since efficiency is prominently advertised in the abstract and conclusion, this part should be tighter.

9. **There is at least one apparent omission/error in the reported results table.**  
   In **Table 1** on Page 7, AIR-Stream MAPE at horizon 12 for STBP appears blank, while the average MAPE is reported as \(29.70\pm0.35\). This is a small but noticeable issue in the main results table. It does not invalidate the entire paper, but it reinforces the general concern that the presentation was not polished carefully enough for a method-heavy submission.

## Questions
1. Please clarify the exact implemented form of DLGA. Is the model using standard softmax attention from Equation (8), a linear-attention approximation with random features, or some hybrid? In particular, what is the exact normalized formula used in code, and what is the actual complexity in \(N\)? A corrected main-text equation would substantially increase my confidence.

2. Can the authors provide an ablation that isolates **FreNet** specifically, rather than only broader variants such as “w/o Backbone” or “w/o DLGA” in **Figure 4**? Since the paper repeatedly attributes drift robustness to the frequency-domain module, a direct “w/o FreNet” comparison is important.

3. How sensitive are the results to the decision to freeze the backbone after the first period? I would like to see comparisons against partial adaptation strategies, such as unfreezing only the prediction head, only the DLGA layers, or only the last block, while keeping parameter budgets comparable.

4. For the conventional baselines in **Table 1**, did the authors attempt stronger continual adaptations beyond the retrain/online setups described in Section 5.2? If not, can they justify why those adaptation protocols are the fairest comparison for those models?

5. For the interpretability story around the contextual pattern bank, can the authors provide quantitative evidence that the learned clusters correspond to meaningful relevance/heterogeneity, rather than relying only on t-SNE visualizations in **Figure 3** and **Figure 6**?

6. Please correct the notation around pattern-bank expansion in Equation (4) and the subsequent paragraph. Which variables denote the inherited bank, the newly added parameters, and the fully expanded bank at period \(\tau\)?

7. Please explain the missing STBP entry for AIR-Stream horizon-12 MAPE in **Table 1**. Is this just a formatting omission?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The application domain is urban forecasting, and the paper does not describe deployment on protected attributes, human-subject data collection, or safety-critical intervention policies requiring a dedicated ethics review. The privacy argument is framed mainly as reduced need to revisit historical raw data, which is reasonable but not itself an ethics red flag.

## Soundness Rating
3: good. The paper has a credible empirical case and the overall method is plausible, but the technical exposition around the core attention equations and some evaluation choices leave nontrivial uncertainty.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures/tables are useful, but the notation, equation-level precision, and some result reporting are not polished enough for a method-centric submission.

## Contribution Rating
3: good. The continual forecasting setting is important, the backbone-plus-pattern-bank decomposition is useful, and the empirical performance appears strong, even if some ingredients are incremental and the technical positioning could be sharper.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem and shows consistently strong empirical results, but the main technical formulation, especially Equations (8) and (9), needs clarification, and the evidence for some of the stronger methodological claims is not as airtight as the narrative suggests.

## Reviewer Confidence
4: confident. I am confident in my assessment and checked the main equations, figures, and results tables carefully, though some uncertainty remains because the implemented attention mechanism is not described as clearly as it should be.