---
job_id: 0f7479a3-d538-4f0d-92b1-f0fb9200ba42
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: tucuU4sQ3s.pdf
paper: Memory-Free Continual Learning with Null Space Adaptation for Zero-Shot Vision-Language Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly in scope for ICLR, specifically continual learning, transfer/lifelong learning, and representation learning for vision-language models.

## Minimum Quality
Pass ✅ The paper includes all core components expected of a research submission, namely abstract, introduction, related work, method, theory, experiments, analysis, and conclusion, and it provides substantial empirical evidence. While I have technical and experimental concerns, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the paper text.

# Expected Review Outcome:
## Summary
This paper proposes NuSA-CL, a memory-free continual learning method for zero-shot vision-language models that computes an approximate null space of current weights via SVD and restricts task-specific low-rank updates to that subspace. The method merges each learned update back into the backbone after every task, with the goal of preserving prior knowledge and zero-shot transfer while maintaining a fixed parameter budget. Experiments on MTIL and class-incremental CIFAR100 show strong performance relative to storage-free baselines, together with favorable compute and memory usage.

## Strengths
The paper addresses a practically relevant problem, continual adaptation of CLIP-like vision-language models without replay buffers, auxiliary distillation models, or growing parameter footprints. That deployment-oriented framing is useful and timely.

The core idea is simple and easy to follow. Constraining updates to a low-energy subspace derived from the current weight matrix is an intuitively appealing way to reduce interference, and the resulting parameterization in Equation 3 is lightweight.

The empirical results are generally strong in the storage-free regime. In **Table 1** on MTIL, NuSA-CL clearly improves over the most relevant storage-free PEFT baselines, namely LoRA and MiLoRA, while using only 1.5M trainable parameters and similar or lower GPU usage. The tradeoff against storage-based methods is also communicated clearly: the paper does not hide that MoE-Adapters and DIKI remain competitive or better in some metrics, but it demonstrates that NuSA-CL is much cheaper.

The few-shot results in **Table 2** are particularly compelling. Under the fixed-backbone PEFT setting, NuSA-CL is consistently competitive across datasets and obtains the strongest summary metrics among compared methods. This is important because few-shot continual learning tends to amplify instability, so the gains there support the paper’s central claim better than a single aggregate full-shot result would.

The long-sequence results in **Table 3** are a meaningful plus. The 50-step CIFAR100 split is a more stressful setting than short task sequences, and NuSA-CL’s advantage over Continual-FT, LwF, and even ZSCL on the reported Last accuracy suggests that the method is not only a short-horizon trick.

The analysis section is more informative than what many empirical continual learning papers provide. In particular, **Figure 2** helps communicate the intended mechanism: compared with Full-FT and LoRA, NuSA-CL shows increasing effective rank and decreasing null ratio across tasks, matching the narrative of gradually using previously low-energy directions instead of repeatedly perturbing dominant directions. Whether this fully proves the mechanism is another question, but as an interpretive diagnostic the figure is useful.

The ablation on subspace choice is also valuable. **Figure 3a** and the corresponding quantitative numbers show that “Tail” directions are better than “Top” or random directions for forgetting, which is exactly the kind of sanity check this paper needs. Likewise, **Table 4a** supports that the persistent constraint matters, rather than the method benefiting merely from another low-rank parameterization.

Presentation is mostly clear. **Figure 1** does a good job summarizing the three-stage pipeline, SVD, constrained adaptation, merge, and the high-level algorithm is understandable from the main paper without having to reconstruct it from the appendix.

## Weaknesses
1. **The central theoretical story is much weaker than the paper’s prose sometimes suggests, because the guarantees are only parameter-space inner-product bounds and do not directly support forgetting claims.**  
   The main technical result, **Lemma 1 / Equation 5** on Page 5, bounds
   \[
   |\langle W,\Delta W\rangle_F| \le \sigma_{k+1}\|M\|_F.
   \]
   This is a statement about correlation between the current weight matrix and the update, not about preservation of predictions, logits, feature geometry, or prior-task risk. The paper does later acknowledge that this is only a “local stability condition rather than a full function-level guarantee,” which is appreciated, but then the surrounding text still leans heavily on phrases like “thereby minimizing interference” and “provides a principled mechanism for mitigating catastrophic forgetting.” That leap is not established by the theorem. In overparameterized neural networks, low Frobenius inner product with the current weights does not by itself imply low functional interference. This matters because the paper’s conceptual hook is stronger than a purely empirical heuristic, and the theory as written does not really carry that burden.

2. **There is a mathematical imprecision in how the “null space” is defined and used, and the terminology is stronger than what the method actually computes.**  
   In **Section 3.1**, the paper defines the “intrinsic null space” as the complement of the top-\(k\) singular directions selected by an energy threshold in **Equation 1**. This is not the null space in the linear algebra sense unless the discarded singular values are exactly zero. The paper occasionally softens this with “approximate null space” or “low-energy subspace,” but the exposition still oscillates between the two. That matters because the mechanism relies on the assumption that low-energy directions are low-interference directions, which is not equivalent to being an actual null space. If the authors want this to read as a principled method rather than a naming flourish, they should be much more precise and consistent about this distinction.

3. **Equation 3 guarantees orthogonality to the principal singular vector subspace only in a narrow matrix-factor sense, and the paper does not fully unpack what that means layerwise or networkwise.**  
   The update
   \[
   \Delta W = U_n M V_n^\top
   \]
   lies in the span of “tail” singular vectors of the current weight matrix. Fine. But the paper then states that this “is mathematically guaranteed to be orthogonal to the principal subspace of \(W\), thereby minimizing interference.” That statement needs more care. The update is orthogonal to the top singular directions under the chosen decomposition, but not necessarily orthogonal to the function-space sensitivity directions induced by activations, nor to past-task gradients, nor even to the dominant directions of the post-merge matrix \(W+\Delta W\). This matters because the strongest alternative methods in continual learning often try to protect gradient or feature subspaces, not weight singular subspaces, and the paper does not really justify why the latter is the right invariant.

4. **The experimental comparison is good within a narrow slice of baselines, but the paper overstates broader state-of-the-art positioning.**  
   The strongest empirical claim is basically “state of the art within practical storage-free PEFT under fixed backbone budget,” which is reasonable. But in **Section 5.2** the wording becomes more expansive, for example “establishes a new state-of-the-art within the practical and challenging storage-free setting” and “superiority of our null-space adaptation strategy.” The evidence supports superiority over the specific baselines included, mostly LoRA, MiLoRA, and InfLoRA. It does not support a broad CL-SOTA claim because the evaluation omits several relevant rehearsal-free continual adaptation families, including weight interpolation or other data-free merge-based strategies, and does not compare against prompt-based rehearsal-free CL methods on the same unified setup. This matters because the paper’s claim to significance depends partly on whether the method beats the right alternatives, not only a subset of them.

5. **The paper’s scope is limited to a single backbone family, and the scalability claim is only partially substantiated.**  
   All experiments use CLIP ViT-B/16. The discussion on Page 10 argues that larger backbones should behave similarly and approximate SVD can be used, but that is speculative in the context of this paper. Since SVD is central to the method, scalability to larger VLMs is not a trivial implementation detail. The method may remain practical, but the paper does not demonstrate this. The concern is not simply “please run bigger models”; it is that the claimed advantage depends on the SVD step remaining cheap relative to training, and that tradeoff may shift materially on larger architectures.

6. **Some of the analysis is mechanistically suggestive but not fully convincing as evidence of “accumulation versus overwriting.”**  
   **Figure 2** is interesting, but the interpretation is a bit too neat. An increase in effective rank after repeated low-rank tail updates is consistent with spectral spreading, but it does not directly show that prior knowledge is preserved because new information is being written into unused capacity. It could also reflect diffuse perturbations that increase spectral entropy without cleanly corresponding to useful task partitioning. The figure supports the narrative, but does not prove it. I would have found it much more convincing if paired with a diagnostic that tracks old-task feature drift or zero-shot text-image alignment drift layerwise.

7. **The “why null space?” ablation is useful, but still narrower than it first appears.**  
   In **Figure 3a** and **Table 10** in the appendix, Tail beats Top and Random in forgetting, which is nice. However, the comparison seems to be framed as a subspace-selection experiment with fixed training budget and low-rank parameterization, not a broader test of alternative continual learning constraints. That means the result mostly shows that, within this specific SVD-guided design space, tail directions are safer than top directions. It does not yet establish that the proposed constraint is better than, say, activation-aware, gradient-aware, or fisher-aware low-rank constraints. This matters because the paper’s main conceptual contribution is exactly the choice of what structure should be protected.

8. **Several details that affect reproducibility and fairness are only partially specified in the main paper.**  
   For example, the main paper says adapters are applied to both vision and text encoders with consistent rank and merged after each task, but it does not clearly specify in the main text whether all \(W_q, W_k, W_v, W_o\) matrices are adapted for all compared LoRA-like methods, or whether any baseline-specific hyperparameters were tuned separately. The appendix clarifies some of this, but the main-paper comparison in **Table 1** and **Table 2** would be stronger if the exact shared tuning protocol were summarized more explicitly there. This matters because PEFT continual learning is quite sensitive to rank, adapter placement, and training budget.

9. **The MTIL metrics are somewhat unusual and the paper could do more to explain what improvements mean in practical terms.**  
   In **Table 2**, the “Overall” column for Avg. and Last appears quite different in scale from the per-dataset AVG column, which can be confusing on first reading. The appendix defines the metrics, but the main paper could explain more carefully how Transfer, Avg., and Last are aggregated and why those numbers should be interpreted together. This is not fatal, but it hurts readability and makes the results tables harder to parse than necessary.

10. **The paper’s literature positioning around null-space methods is incomplete.**  
   The related work covers InfLoRA, MiLoRA, and some SVD-guided adaptation papers, which are relevant. However, for a paper whose identity is built around null-space adaptation in a continual or data-free setting, the broader positioning feels narrower than it should. There are adjacent strands on rehearsal-free adaptation via weight interpolation / merging and null-space filtering ideas that would help readers understand what is genuinely new here versus what is a specific instantiation for CLIP-style continual adaptation. This matters because the originality of the work is not only in using SVD, but in how that choice is differentiated from nearby “do-no-harm” adaptation strategies.

11. **There are places where the paper’s wording is a bit too absolute relative to the evidence.**  
   Examples include phrases like “strictly confines all weight updates within these interference-free dimensions” in the introduction and “This additive learning process is the core mechanism behind NuSA-CL’s ability to mitigate catastrophic forgetting” in the analysis. These phrases are rhetorically strong. But the subspace is only approximate, the interference notion is only parameter-space, and the empirical gains, while strong, are not uniformly dominant over all storage-based baselines in **Table 1**. This overstatement does not invalidate the method, but it does make the paper sound more airtight than it actually is.

## Questions
1. The main theoretical argument is based on \(\langle W,\Delta W\rangle_F\). Can the authors provide stronger empirical evidence that this correlates with actual forgetting, for example by plotting this quantity against old-task accuracy drop across tasks and layers? A rebuttal with such evidence would increase my confidence that the theoretical lens is not merely decorative.

2. How sensitive are the results to *where* SVD is applied? The appendix says attention projections are adapted, but does the method still hold if only \(W_q/W_v\) are used, or if MLP layers are included? This matters for understanding whether the gains come from the null-space idea itself or a particular layer-selection choice.

3. In **Equation 3**, why is \(M\) chosen as a full \(r \times r\) trainable matrix rather than a further factorization such as \(AB^\top\)? Is there an empirical or conceptual reason this parameterization is preferable beyond convenience?

4. Can the authors clarify whether the SVD is full or truncated in all reported experiments, and what exact wall-clock fraction of total runtime it occupies per task? **Table 4b** reports “<1 min” initialization, which is helpful, but a more granular per-task cost breakdown would strengthen the practicality claim.

5. The paper argues, especially via **Figure 2**, that NuSA-CL accumulates knowledge rather than overwriting it. Can the authors provide an additional representation-space diagnostic, such as CLIP embedding drift on previous tasks or text-image similarity preservation before/after each task? That would directly test the intended zero-shot preservation story.

6. For the MTIL comparisons in **Table 1** and **Table 2**, how were hyperparameters selected for LoRA, MiLoRA, InfLoRA, and NuSA-CL? Was there a shared validation protocol, and was task order fixed during tuning? Since small PEFT methods can be quite sensitive, this could affect how decisive the reported margins should be interpreted.

7. The long-sequence CIFAR100 result in **Table 3** is promising. Do the authors have evidence on whether the method remains stable under different class orders or repeated runs? Even a small variance estimate would make the scalability claim more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are apparent from the paper. The work studies continual adaptation of standard vision-language models on established benchmarks and does not introduce a dataset, deployment claim, or application domain that raises a distinct ethics concern beyond the usual downstream risks of foundation models.

## Soundness Rating
3: good. The method is technically plausible and supported by solid experiments, but the theory is limited to a weak surrogate notion of interference, and some claims are stronger than the evidence strictly justifies.

## Presentation Rating
3: good. The paper is generally clear, well organized, and helped by useful figures and tables, though some terminology, metric explanations, and theoretical wording need tightening.

## Contribution Rating
3: good. The paper makes a meaningful contribution to memory-free continual adaptation for CLIP-like models, especially in the storage-free PEFT regime, but the novelty and broader positioning are not strong enough for a higher score.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The empirical case is strong enough, particularly in the storage-free setting, that I lean positive, but the theoretical justification is weaker than advertised and the paper overreaches somewhat in its interpretation and state-of-the-art framing.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the method, equations, figures, and main empirical comparisons carefully, though broader baseline coverage and additional diagnostics could still shift my confidence somewhat.