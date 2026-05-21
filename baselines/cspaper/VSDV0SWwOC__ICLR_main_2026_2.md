---
job_id: 9a684f8a-6a3e-4354-a645-c670c9051499
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: VSDV0SWwOC.pdf
paper: LS-Merge: Merging Language Models in Latent Space
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning and generative modeling in neural network weight space, with applications to LLM model merging and cross-architecture transfer.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments, quantitative results, discussion, and conclusion. While there are important weaknesses in methodological specification and evaluation depth, the paper is complete enough and technically substantive enough to warrant full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, review-targeting instructions, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes LS-Merge, a framework for merging language models in a learned latent space rather than directly in weight space. The method uses a transformer-based VAE to encode chunked model weights, performs interpolation in latent space, and introduces a proportional dimensionality-matching scheme plus OT-based alignment for heterogeneous merges across models with different sizes or families. Empirically, the paper evaluates self-merging, LoRA expert merging, representation-merging comparisons, cross-architecture merging, and several ablations on Gemma, LLaMA, and expert-fusion settings.

## Strengths
The paper tackles an important and timely problem. Weight-space merging is useful but often brittle under architecture mismatch, and the paper squarely targets that limitation rather than only reporting another same-architecture merge recipe. The focus on heterogeneous merging is meaningful and relevant to current LLM practice.

The overall framework is intuitive and reasonably well motivated. **Figure 1** is effective in communicating the encode, align, interpolate, decode pipeline, especially the distinction between homogeneous and heterogeneous merging. That figure helps anchor the paper’s central claim that latent space can act as a common interface across incompatible parameterizations, which is the main conceptual contribution here.

The empirical section is broader than many papers in this area. The paper does not stop at one benchmark, but includes self-merging, LoRA expert fusion, comparison to activation/representation merging methods, heterogeneous intra-family transfer, cross-family transfer, and compression ablations. That breadth is a real positive.

Some of the experimental results are genuinely promising. In particular, **Table 3** shows consistent gains of LS-Merge over several direct weight-space baselines on the LoRA expert setting. The margins on HellaSwag, MMLU, and K-Crossword are not trivial, and the improvement over both simple soups and SLERP suggests the method is not merely matching weak baselines by noise. Similarly, **Table 4** shows LS-Merge to be competitive with AIM while clearly outperforming Task Arithmetic in that setup, which is a useful result for the community.

The paper also makes a decent effort to probe why the method might work. **Table 8** is one of the stronger pieces of evidence in the paper, because it directly compares the proposed nonlinear encoding against PCA under matched compression ratios. The fact that PCA reconstruction largely destroys functional performance while the VAE mostly preserves it supports the authors’ argument that a nonlinear manifold view is more appropriate than a simple linear subspace picture.

The heterogeneous merging story is supported by at least some direct evidence. **Figure 4** is useful here: panel (a) shows that OT-aligned latent interpolation can improve over the smaller target baseline in a constrained mixing regime, while panel (b) usefully illustrates that interpolation without alignment is unstable and that the choice of interpolation coefficient matters. Even though I have concerns about the depth of this analysis, the figure does support the claim that alignment is not just decorative.

The paper is also commendably explicit about some limitations, especially the compression/generalization trade-off and the difficulty of training the VAE at higher compression. That makes the submission feel more honest than papers that only report best-case wins.

## Weaknesses
My main issue is that the core method is under-specified in several places, and this matters because the paper’s contribution depends heavily on seemingly small design choices.

First, the mathematical formulation around the VAE and encoder/decoder notation is sloppy enough to create avoidable confusion. In **Equation (1)** on **Page 5**, the ELBO is written as
\[
\mathcal{L} = - \mathbb{E}_{q_{\phi}(z\mid w)}[\log p_{\theta}(w\mid z)] + \beta \mathrm{KL}(q_{\phi}(z\mid w)\|p(z)).
\]
But in the surrounding text, the encoder is denoted \(E_{\theta}\) and decoder \(D_{\phi}\), which reverses the conventional association of encoder and decoder parameters relative to the equation. This is not fatal by itself, but it reflects broader notation inconsistency. More importantly, the paper never clearly specifies the actual likelihood model for \(p(w\mid z)\), the reconstruction loss used in practice, whether weights are modeled with Gaussian noise, whether losses are normalized per chunk or per layer, and how padding is masked. Since the whole point is to preserve heavy-tailed parameter information, the exact reconstruction objective matters a lot. A Gaussian decoder with plain MSE behaves very differently from, say, a robust loss or heteroscedastic decoder. Right now that core design choice is left implicit.

Second, the theoretical motivation in **Section 3.1** overreaches relative to what is actually established. The argument moves from low-rank structure in individual matrices and PCA explained variance in **Figure 2** to claims about the existence of a low-dimensional manifold for model weights, and then to the claim that a VAE can approximate an appropriate compressive embedding. This chain is much too quick. The Eckart-Young result applies to approximating a single matrix, not to the geometry of the set of functionally valid checkpoints. The manifold embedding statement is also presented in a hand-wavy way, with undefined or inconsistent quantities, for example the formula around \(k = O(\frac{d}{\sqrt{s}}\log \frac{V}{\varepsilon})\) on **Page 4** introduces symbols that are not properly contextualized in the main text, and the sentence itself is grammatically broken. The result ends up sounding stronger than warranted. This matters because the paper repeatedly appeals to geometric necessity, especially later in the PCA comparison.

Third, the heterogeneous alignment mechanism is not specified precisely enough for reproducibility or for evaluating whether the OT story is really doing what the paper claims. In **Equation (2)** and the text on **Pages 5-6**, the paper starts from the Monge formulation, then says that each layer’s latent distribution can be approximated as a high-dimensional Gaussian and gives the affine Bures-Wasserstein map
\[
\tilde z_{\text{src}} = \mu_t + A(z_{\text{src}}-\mu_s), \quad
A = \Sigma_s^{-1/2}(\Sigma_s^{1/2}\Sigma_t\Sigma_s^{1/2})^{1/2}\Sigma_s^{-1/2}.
\]
However, the practical details are missing. Are \(\mu_s,\Sigma_s,\mu_t,\Sigma_t\) estimated per layer over chunks within one checkpoint, over many checkpoints, or over stochastic posterior samples? How is covariance regularized when the latent dimension is large relative to the number of chunks? What happens if \(\Sigma_s\) is rank-deficient, which seems plausible in this setting? The statement “we use existing OT library” is not an adequate substitute for specifying the actual estimator. Since the heterogeneous result rests on this alignment, these details are not peripheral.

Fourth, the algorithms as written are error-prone to the point that they reduce confidence. **Algorithm 1** on **Page 6** contains multiple typos and inconsistent variable names, such as “ltrc”, “lgt”, “wtrc, wgt, wgt”, and line 6 seems malformed: \(Z_\lambda \leftarrow (1-\lambda) Z_{\text{gt}} \leftarrow \lambda Z_{\text{trc}}\). **Algorithm 2** in the appendix is even worse, with several lines that are clearly broken placeholders rather than a faithful algorithmic description, such as “\(z^{(1)} \to OT(z^{(1)}, z^{(1)})\)” and “Decode: \(w^{(1)} \to (z^{(1)} + w^{(1)})\).” I understand the review should be based on the main paper, but when the main-paper algorithm is itself malformed and the appendix version is clearly corrupted, it raises concerns that the implementation details are not being communicated carefully.

Fifth, the empirical comparisons, while broad, are not always as convincing as the claims suggest. The paper repeatedly claims robustness and stronger downstream performance, but the evaluation protocols vary across sections in ways that make direct interpretation harder. For example, **Section 4.3** explicitly switches to lm-eval “for fair comparison,” and **Section 4.4** says cross-family evaluation also uses lm-eval due to issues with the prior evaluation code. That is understandable operationally, but it weakens comparability across tables. Also, **Table 2** reports gains from “self-merging,” but the exact sampling procedure is not clearly defined. How many posterior samples are drawn, how they are combined, whether \(\lambda\) is tuned on validation data, and whether any test-informed model selection occurred are all unclear. Since self-merging is one of the headline claims, that ambiguity matters.

Sixth, some of the quantitative evidence is thinner than the prose implies. **Figure 4(a)** shows gains for Gemma-3-4B-it \(\rightarrow\) Gemma-3-1B-it, but only on MMLU and MMLU-Pro, and only for a narrow interpolation region. The paper’s takeaway on **Page 8** says that “a single knob \(\lambda\) reliably controls how much capacity is injected,” but the figure actually suggests a fairly delicate regime where small injections help and larger ones can hurt. That is a useful finding, but it is not the same as a robust, well-behaved control knob. Likewise, **Figure 3** is visually suggestive, but the claim that the merged latent “partially overlapped with the target latent” is not a strong validation of successful alignment. The figure would be more convincing with quantitative overlap metrics or downstream performance tied directly to the visualization.

Seventh, there are missing or insufficiently discussed baselines in the heterogeneous setting. The paper cites existing weight-space merging and modular assembly methods, but for the actual cross-architecture claim, the comparison set is light. In **Table 5**, the alignment ablation is only “Base,” “OT only,” and “OT + interp.” This shows OT helps relative to naive baselines within the proposed framework, but it does not establish competitiveness against stronger cross-architecture alternatives. Given that heterogeneous merging is the most distinctive part of the paper, stronger direct baselines there would substantially improve the submission.

Eighth, the interpretation of the compression experiments is internally inconsistent. On **Page 9**, **Section 5.2** says performance at higher compression ratios degrades substantially and suggests posterior collapse. Yet **Table 8** on **Page 10** reports VAE performance that is strikingly stable even at \(r=4.0\), with MMLU 39.83 versus 39.89 at \(r=1.6\), and ARC-C even slightly improves. That is hard to reconcile with **Table 7**, where \(r=4\) leads to substantial degradation on unseen models. I think the intended distinction is probably in-distribution reconstruction versus zero-shot generalization, but the paper does not explain this clearly enough, so the narrative currently sounds contradictory.

Ninth, the paper’s related-work positioning is somewhat too sweeping. The statement in **Section 2** that “All prior methods operate in weight or module space and assume architectural alignment” is stronger than necessary and likely too broad. Even within the authors’ own framing, there are prior efforts on heterogeneous assembly and cross-topology/model merging that should be discussed more carefully if the paper wants to claim a clean first move in this direction. The current positioning risks understating adjacent literature.

Finally, the presentation has many local issues that accumulate. There are repeated grammatical errors, notation switches, malformed equations/text snippets, and table/figure references that are awkwardly integrated. A concrete example is **Table 5 and Table 6** on **Page 9**, which appear jammed together in a way that makes the captioning hard to parse. Another is the statement around the latent dimension formula on **Page 4**, which seems partially corrupted. None of these individually kill the paper, but for a method-heavy submission, they do reduce confidence.

## Questions
1. Please specify the exact reconstruction model used in **Equation (1)**. Is the reconstruction term plain MSE on normalized weights, Gaussian negative log-likelihood with fixed variance, or something else? How are zero-padding and variable-length chunks masked in the loss?

2. For self-merging in **Section 4.1**, what is the exact sampling and averaging protocol? How many latent samples are drawn per model, are they sampled from \(q(z\mid W)\) or from the prior, how are merge coefficients chosen, and was any hyperparameter selected using test-set performance? A precise answer here would increase confidence.

3. For heterogeneous OT alignment in **Section 3.3**, how exactly are \(\mu_s,\Sigma_s,\mu_t,\Sigma_t\) estimated? Are these per-layer statistics over chunks from a single checkpoint, over multiple checkpoints, or over posterior samples? How do you regularize covariance square roots and inverses when the empirical covariance is low-rank or ill-conditioned?

4. Can the authors provide a stronger heterogeneous baseline comparison, beyond the internal ablation in **Table 5**? This is the most distinctive claim of the paper, so evidence against stronger cross-architecture alternatives would materially affect my assessment.

5. Please reconcile the apparent discrepancy between **Table 7** and **Table 8**. Why does \(r=4\) look catastrophic for zero-shot transfer in Table 7 but largely harmless for reconstruction fidelity in Table 8? If the answer is in-distribution versus out-of-distribution behavior, please state that explicitly and quantify it.

6. In **Figure 4(b)**, performance appears sensitive to the interpolation coefficient. How is \(\lambda\) chosen in practice for heterogeneous merges, and how stable is the best range across tasks and model pairs? If the range is narrow, the “reliable single knob” claim should probably be softened.

7. The paper argues from **Figure 2** and **Table 1** that heavy tails and low-rank structure motivate the VAE. Have you tried any tail-aware reconstruction objectives or priors, such as Laplace/Student-\(t\) reconstruction or robust losses? Since the motivation emphasizes heavy-tailed weights, this seems like a natural and potentially important ablation.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper proposes methods for combining pretrained LLMs and experts into a single model, including cross-family and cross-architecture transfer. As also acknowledged in the appendix impact statement, such tooling could facilitate capability grafting, provenance obfuscation, or the transfer of harmful behaviors between models. I do not see an ethics violation in the submission itself, but this is a model-composition method with plausible misuse potential, so a light ethics review on downstream misuse and provenance considerations would be appropriate.

## Soundness Rating
3: good. The paper is technically plausible and supported by a reasonably broad empirical study, but several core methodological details, especially around the VAE objective and OT alignment, are underspecified, and some claims are stronger than the evidence provided.

## Presentation Rating
2: fair. The high-level story is understandable and some figures, especially Figure 1 and Figure 4, are helpful, but the paper suffers from notation inconsistencies, malformed algorithm descriptions, and several places where the exposition is not careful enough for a method-centric paper.

## Contribution Rating
3: good. The idea of moving LLM merging into a learned latent weight space, particularly for heterogeneous merging, is interesting and valuable to the community, even if the experimental and methodological case is not yet as airtight as the paper claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem and presents a promising direction with several strong empirical results, especially for expert fusion and heterogeneous merging. However, I have nontrivial concerns about specification, positioning, and the depth of validation for the OT-based heterogeneous story. I lean positive because the central idea is useful and the empirical evidence is better than a typical borderline paper, but this is not an easy accept.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant areas of model merging, generative modeling over weights, and representation learning, though some implementation details are underspecified enough that there is still room for author clarification.