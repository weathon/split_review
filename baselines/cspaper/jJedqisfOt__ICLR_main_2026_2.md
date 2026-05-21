---
job_id: 6438e534-42f5-442a-a0a3-95205f41ee29
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: jJedqisfOt.pdf
paper: Neural Dynamics Self-Attention for Spiking Transformers
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning architectures for vision using spiking neural networks and Transformer-style attention, with emphasis on efficiency, memory, and inductive biases.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments, quantitative results, qualitative analysis, and conclusion. While I found substantial concerns about mathematical rigor, exposition, and empirical support, these issues do not rise to the level of an obvious desk rejection based on the manuscript alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, reviewer-directed instructions, or other manipulative content in the provided manuscript text and figures.

# Expected Review Outcome:
## Summary
This paper studies two stated limitations of existing spiking self-attention in Spiking Transformers, namely weak locality bias relative to vanilla softmax attention and large inference-time memory overhead due to storing attention-related matrices. To address these, the authors propose LRF-SSA, which augments spiking self-attention with local receptive field terms, and LRF-Dyn, which further re-expresses the computation through neuron-inspired dynamics to reduce memory complexity. Experiments on ImageNet-1K classification, ADE20K semantic segmentation, and CIFAR-100 ablations report accuracy improvements over several spiking Transformer backbones, together with reduced storage complexity for LRF-Dyn.

## Strengths
The paper targets a real and relevant problem for spiking Transformers. The gap between ANN-style Transformer performance and spike-friendly efficiency claims is important, and the paper tries to address both modeling quality and deployment constraints rather than only accuracy.

The proposed direction is reasonably intuitive. Injecting locality bias into SSA is a sensible design choice, especially in vision, where pure softmax-free global attention often underuses spatial structure. The second step, replacing explicit attention computation with a recurrent neuronal-dynamics-style formulation, is also interesting from a systems perspective because it tries to align the architecture with the memory constraints that motivate SNNs in the first place.

The empirical scope is broader than many papers in this area. Table 1 evaluates three spiking Transformer families, Spikformer, QKFormer, and SDT-V3, and the gains are fairly consistent across scales. Even if the margins are modest in some settings, the fact that improvements appear across multiple backbones is a meaningful positive signal.

The qualitative evidence is directionally supportive. In Figure 5(a), the effective receptive field visualizations are consistent with the paper’s central claim that vanilla SSA is overly diffuse and that both LRF-SSA and LRF-Dyn recover stronger locality. Likewise, Figure 4 shows qualitatively sharper attention heatmaps and better segmentation boundaries for the proposed variants than SSA, which is aligned with the intended mechanism.

The paper also makes an effort to provide some theoretical framing rather than only an engineering recipe. Although I have several reservations about the rigor of that analysis, the attempt to relate entropy, receptive field size, and attention distributions to the architectural modification is a legitimate strength in intent.

## Weaknesses
I have substantial concerns about the paper’s technical rigor and clarity. The core idea is plausible, but several mathematical statements, complexity claims, and experimental choices are not presented carefully enough for me to fully trust the conclusions.

1. **The theoretical analysis in Section 5 is much weaker than the paper claims, and parts of it appear internally inconsistent.**  
   Theorem 1 on Page 5 states that VSA has weights $\alpha_{ij}^{vsa}\propto \exp(-\beta \Delta)$ and SSA has $\alpha_{ij}^{ssa}\propto(\alpha-\beta\Delta)_{+}$. This is not derived from the actual SSA definition in Equation (5), which is based on dot products of spike-generated $Q$ and $K$, not on a predefined distance-decay law. The theorem therefore studies a stylized surrogate model rather than the proposed method itself. That is not necessarily invalid, but the paper presents it much more strongly than warranted, as if it establishes the actual behavior of SSA in practice. The same issue appears in Theorem 2, where entropy comparisons are stated under hand-crafted distance distributions rather than the learned attention produced by the model. This matters because the headline scientific claim, namely that lack of locality in SSA explains the performance gap and that LRF restores VSA-like properties, rests heavily on these arguments.

2. **There are multiple notation and derivation problems that make the method difficult to verify.**  
   Equation (8) on Page 5 is especially problematic. The global term is written as
   \[
   \mathrm{sattn}_{n}^{\prime}[t]=\mathrm{q}_{n}[t]\times\sum_{j=1}^{N}k_{j}[t]^{T}v_{j}[t]+\sum_{d\,i,j\in\Omega_{d}}r_{ij}^{d}\mathbf{V}^{\rho_{k}}.
   \]
   The local term is underspecified: $\mathbf{V}^{\rho_k}$ is not properly defined, the indexing over $d,i,j$ is compressed in a way that is ambiguous, and dimensional consistency is not obvious. Equation (11) inherits the same issue, and the “presynaptic input” mixes a self-term $k_n[t]^T v_n[t]$ with local receptive field contributions in a way that is more descriptive than formally defined. Then Equation (12) abruptly introduces $\mathrm{Token}_n[t]$, $\mathcal{A}$, and $\Gamma$ without giving a derivation that shows how this is an approximation of Equation (11). By the time we reach Equations (13) and (15), the symbols have drifted again: $\Gamma$ becomes $\gamma$, $\mathcal{A}$ is defined by a matrix product with unclear shape, and $\mathcal{K}(t)$ in Page 7 is mentioned without being clearly connected to the preceding dynamics. This is not a cosmetic issue, it makes the central mechanism hard to reproduce or even assess for correctness.

3. **The claimed memory and complexity reductions are not cleanly established.**  
   Section 4.2 and Section 5.2 repeatedly discuss storage complexity, but the manuscript mixes several different notions: storing $QK$ matrices of size $N^2$, storing $KV$ matrices of size $d^2$, storing membrane states, and using causal reformulations. For example, Page 6 says that Equation (11) reduces “the computational complexity $\mathcal{O}(Nd^2)$ to $\mathcal{O}(d^2)$,” which sounds like a reduction in compute, but the surrounding text is about memory. Later, Table 1 reports “SR.” as storage complexity and lists $O(d^2)$ or $O(kd)$, while Figure 5(b) visualizes memory usage reductions, but the paper never provides a precise accounting protocol. Is this peak activation memory, persistent state memory, or a hardware-specific estimate? These are not interchangeable. Given that memory reduction is one of the two main claimed contributions, the evaluation should be much more rigorous and explicit.

4. **Figure 1 and Figure 2 support the intuition, but the causal claim that locality mismatch is the main reason for the performance gap is overstated.**  
   Figure 1(a) and Figure 2 do show that the chosen VSA attention maps are more localized than SSA, and Figure 2(c,d) suggests lower entropy for VSA. But the manuscript jumps from this observation to a broader explanation for the ANN-SNN performance gap. That is too strong. Many other factors differ between VSA and SSA, including quantization/spiking nonlinearities, temporal coding, optimization difficulty, architectural details, and the absence of softmax normalization itself beyond locality effects. The paper does not isolate locality as the dominant factor. The ablations in Table 3 show that adding larger local kernels improves accuracy, which supports usefulness, but not exclusivity or primary causality.

5. **The empirical evidence is promising but still incomplete for the paper’s central claims.**  
   Table 1 is the strongest part of the evaluation, and the cross-backbone consistency is good. However, the paper does not report variance across runs, confidence intervals, or even whether the reported gains are single-run numbers. Several gains are relatively small, for example $+0.41\%$, $+0.44\%$, $+0.48\%$, and without any measure of variability it is hard to judge robustness. This is particularly important in SNN training, where optimization can be unstable. The appendix is said to contain convergence plots, but the main paper should still include at least basic run-to-run stability information when the margins are this tight.

6. **The segmentation results in Table 2 are hard to interpret because the table organization is confusing and some comparisons are not apples-to-apples.**  
   Table 2 appears to interleave baseline and proposed rows in a way that obscures which parameter count corresponds to which method. For instance, “SDT-V3” and “+ LRF-SSA” are split across rows, and the parameter counts jump from “5.1 + 1.4” to “10.0 + 1.4” and from “18.99 + 1.4†” to “19.25 + 1.4,” but the formatting makes it unnecessarily hard to parse. More importantly, LRF-SSA appears to add a substantial number of parameters in the smaller segmentation model, which sits awkwardly with the earlier claim on Page 7 that it introduces “almost no additional parameters.” If the segmentation head or decoder is responsible for the larger increase, that should be explained explicitly. Right now the paper seems to want credit both for negligible overhead and for gains that may partially come from nontrivial extra capacity.

7. **The relationship between LRF-SSA and LRF-Dyn is not adequately validated as an approximation claim.**  
   The paper says LRF-Dyn approximates or reformulates LRF-SSA through neuronal dynamics, but there is no direct approximation study in the main paper. I would expect at least one controlled experiment comparing attention outputs or feature similarity between LRF-SSA and LRF-Dyn, or a derivation showing under what assumptions Equation (12) approximates Equation (11). Instead, the paper mostly shows that LRF-Dyn performs similarly in accuracy while using less memory. That is useful, but it does not validate the claimed mechanism. Similar empirical performance alone does not establish that the dynamics implement attention in the proposed sense.

8. **Some claims around biological inspiration feel more rhetorical than scientifically operationalized.**  
   Figure 3 is visually appealing and the analogy to dendritic processing is interesting, but the paper leans heavily on biological terminology, such as soma, dendrites, membrane potential, and presynaptic input, without always showing how these constructs materially constrain or justify the architecture. In Figure 3(c), the “LRF-Dyn” block is presented as replacing attention with a dendritic neuron, but the actual implementation in Equations (12)-(15) still reads like a custom recurrent filtering module with local convolutions. That is not necessarily a weakness by itself, but the manuscript sometimes oversells the biological grounding relative to the formal content.

9. **There are concrete mathematical inconsistencies in the appendix that reduce confidence in the theorems summarized in the main paper.**  
   Although my judgment is based on the main paper, the appendix exposes issues with the stated proofs. In Appendix C.2, Equation (3) is labeled as SSA but then gives an exponential form, which is the VSA-style distribution. Later, the text says “As $n\to\infty$, the expected receptive radius of VSA can be defined as follows” immediately before giving $\mu_\infty^{ssa}$ in Equation (6), which is clearly inconsistent. The notation also flips between $\alpha$, $a$, “lra-ssa” and “lrf-ssa.” These may be editing mistakes, but when the core theorems already rely on stylized assumptions, this sloppiness materially weakens confidence in the analysis.

10. **Presentation quality is below the level expected for a method paper with this many equations.**  
   There are many grammar and wording issues that are minor individually but costly collectively. A few examples: “we propose a Local Receptive Field methods into SSA” on Page 2, “this computations” on Page 5, “causal inference” on Page 6 when “causal/recursive reformulation” seems intended, and “The proposed method produces more fine-grained segmentation results, whereas SSA tends to yield only localized segmentations” on Page 8, which is both vague and oddly phrased. More importantly, the notation is not stable across sections. For a paper whose main novelty is a new mathematical reformulation, that is a serious presentation problem rather than a superficial editorial one.

11. **The literature positioning around efficient or locality-aware spiking attention is somewhat thin.**  
   The paper cites several important spiking Transformer works, but the related work discussion is still quite narrow relative to the claimed contribution. Since the main claims involve restructuring spike-based attention for locality and memory efficiency, the paper would benefit from a more careful comparison against other spiking attention variants that also modify the attention structure or trade off global context for efficiency. The current positioning makes the method look more isolated than it actually is, which weakens the novelty argument.

12. **The qualitative figures are supportive but also expose gaps in the evaluation protocol.**  
   Figure 4 is used to claim “ViT-like attention patterns but with sparser distributions” and finer segmentation outputs. However, these visualizations are anecdotal. The paper does not quantify sparsity, entropy, or localization improvements across the dataset. Figure 5(b) similarly makes a strong visual claim about the accuracy-memory tradeoff, but the exact memory metric and measurement setup are not stated. For a paper centered on memory efficiency and locality, these should not be left at the level of illustrative plots.

Overall, I see the intuitive appeal of the proposal and I do believe the empirical results indicate that adding locality helps. But the paper currently overclaims on theory, under-specifies the core derivation of LRF-Dyn, and does not evaluate the memory argument with enough rigor to justify a positive recommendation.

## Questions
1. **Can the authors provide a clean, dimensionally consistent derivation from Equation (8) to Equation (11), and then from Equation (11) to Equation (12)?**  
   In rebuttal, I would like a line-by-line explanation of shapes and symbols, especially for the local term involving $\rho_k$, $r_{ij}^d$, and the transition from explicit $k_j^\top v_j$ aggregation to the recurrent state $\mathrm{X}_n[t]$. This is the most important clarification for increasing my confidence.

2. **What exactly is the memory metric used in Table 1 and Figure 5(b)?**  
   Is “SR.” peak intermediate activation storage during inference, total persistent state, per-layer memory, or a theoretical asymptotic proxy? Please define the measurement protocol and, ideally, report actual measured memory consumption in MB for at least one architecture and input size, in addition to asymptotic notation.

3. **How stable are the reported gains across random seeds?**  
   Please provide mean and standard deviation over multiple runs for at least the main ImageNet and CIFAR-100 results, especially for the smaller improvements in Table 1. This would help determine whether the gains are robust.

4. **Can the authors directly validate LRF-Dyn as an approximation of LRF-SSA rather than only as a separate module with similar accuracy?**  
   For example, compare feature similarity, output similarity, or token interaction statistics between the two modules under matched settings. Without this, the “implements attention through neuronal dynamics” claim feels under-supported.

5. **How much of the segmentation gain in Table 2 is attributable to additional parameters versus the proposed mechanism itself?**  
   Please clarify the parameter accounting in that table and, if possible, include a capacity-matched comparison.

6. **Can the authors quantify the locality/entropy hypothesis more rigorously across the dataset?**  
   Figure 2 and Figure 5(a) are suggestive, but a systematic metric, such as average attention entropy, average Manhattan distance, or effective receptive field radius over validation samples, would better support the central premise.

7. **What assumptions are required for Theorem 1 and Theorem 2 to meaningfully describe the learned models?**  
   If these are only toy analyses under a distance-decay model, the paper should say so clearly and soften the claims. If the authors believe the theorems are more directly descriptive of the trained architectures, that connection needs to be justified.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics issues stood out from the manuscript. The work focuses on architectural design and evaluation on standard vision benchmarks.

## Soundness Rating
2: fair. The empirical results are encouraging, but the main technical claims are only partially supported. The mathematical derivations and complexity arguments need clearer and more rigorous justification.

## Presentation Rating
2: fair. The paper is readable at a high level, but notation drift, underspecified equations, and several confusing passages significantly reduce clarity.

## Contribution Rating
2: fair. The locality-enhanced SSA idea is useful and the cross-backbone experiments are relevant, but the overall contribution feels not yet solid enough in rigor and validation for a stronger score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and shows promising empirical gains, but the current version overstates its theory, under-specifies the LRF-Dyn derivation, and does not support the memory-efficiency claim with enough rigor.

## Reviewer Confidence
4: confident. I am familiar with spiking networks, efficient attention, and vision architectures, and I checked the main derivations and empirical claims carefully. Some uncertainty remains because the presentation obscures parts of the method.