---
job_id: 6db85335-7f33-4531-ad78-4ec5ed9ea5e0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GMP1S4R6Ke.pdf
paper: LoRA-Mixer: Coordinate Modular LoRA Experts Through Serial Attention Routing
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, focusing on parameter-efficient adaptation, mixture-of-experts routing, representation learning in LLMs, and optimization of routing objectives.

## Minimum Quality
Pass ✅ The paper contains the required scientific structure, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, and Conclusion. While there are important issues in clarity, theory-to-practice alignment, and experimental rigor, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes LoRA-Mixer, a framework for combining multiple LoRA adapters as experts by inserting routed LoRA mixtures into linear projection layers, especially attention projections, rather than mainly routing in FFN blocks or using shallow parallel branches. The paper also introduces Routing Specialization Balance Loss (RSL), an entropy-regularized routing objective intended to balance global load balancing with token-aware specialization, and evaluates the method across several base models and a broad collection of benchmarks, including Transformer and SSM architectures.

## Strengths
The paper addresses a practically relevant problem, namely how to compose multiple LoRA modules in a modular and parameter-efficient way without fully retraining everything. This is a useful direction for the ICLR community, especially given the increasing interest in PEFT plus expert routing for multi-task adaptation.

The architectural idea is intuitive and reasonably motivated. In **Figure 1** on **Page 2**, the contrast between replacing whole FFN/attention blocks, attaching parallel LoRA branches, and the proposed projection-level integration makes the design choice easy to understand. The core pitch, routing LoRA experts inside projection layers that sit directly on the model’s main computation path, is more compelling than a generic “we also do MoE with LoRA” story. **Figure 2** on **Page 3** also helps convey the intended breadth across Transformer and SSM-style blocks.

The empirical section is broad. Even though I have reservations about some comparisons, the paper does test across multiple model families and tasks, including Falcon-Mamba, Mistral, and LLaMA variants, and it includes both “train experts jointly” and “reuse pre-trained LoRAs” style settings. That breadth is a genuine plus.

Several result tables suggest the method is consistently competitive. In **Table 2** on **Page 7**, LoRA-Mixer is usually the top-performing method across the listed settings, and in the LLaMA-3 block it improves over LoRA, MoLE, MixLoRA, and LoRAHub on all seven reported tasks. The gains are not huge everywhere, but they are fairly consistent, which is more convincing than a single cherry-picked win. **Table 8** on **Page 8** is also a strength for the paper’s routing-loss claim, since under the same reported 2k-data condition RSL outperforms GMoE, DS-MoE, and AESL across all listed tasks.

The paper includes some analysis beyond headline accuracy. **Table 9** on **Page 9** is useful because it directly addresses the low-data routing claim and shows that RSL is most helpful in the smaller-data regime. Likewise, **Figure 4** on **Page 9** attempts to visualize the distinction between RSL and vanilla auxiliary loss, which is aligned with the paper’s central claim that standard balancing losses flatten routing too much.

The method’s compatibility with SSMs is a nice practical angle. Many LoRA-MoE papers stay entirely inside Transformer-centric formulations; here the authors at least make a concrete attempt to demonstrate portability to Falcon-Mamba.

## Weaknesses
1. **The mathematical formulation of the core model is underspecified, and in places internally inconsistent.**  
   The biggest issue is **Equation (4)** on **Page 4**:
   \[
   \mathbf{y}=W\mathbf{x}+\mathcal{F}_{\text{route}}\left(\left\{\alpha_{e}(\mathbf{x})\cdot\Delta W^{(e)}\mathbf{x}\right\}_{e=1}^{E}\right).
   \]
   This does not actually define the routing computation in a usable way. What exactly is \(\mathcal{F}_{\text{route}}\)? Is it just summation over top-\(k\) experts, a weighted sum, a sparse mask plus renormalization, or something else? The notation suggests the router outputs \(\alpha_e(x)\), but then a second routing function \(\mathcal{F}_{\text{route}}\) is applied on the already weighted expert outputs. This creates ambiguity about whether routing happens in score space, output space, or both. Since the entire paper hinges on “serial attention routing,” the forward pass should be written explicitly, for example
   \[
   y = Wx + \sum_{e \in \mathrm{TopK}(p(x))} \tilde p_e(x)\, A^{(e)}B^{(e)}x,
   \]
   together with a definition of \(\tilde p_e\), top-\(k\) masking, and whether gradients flow through hard top-\(k\) or a soft approximation. As written, the method is not crisply specified enough in the main paper.

2. **The RSL objective is not cleanly defined, and the paper switches between incompatible notions of usage.**  
   In **Equation (3)** on **Page 4**, \(\bar f_i\) is defined as top-1 empirical usage:
   \[
   \bar f_i = \mathbb{E}_{x \sim \mathcal D}[\mathbb{I}(i=\arg\max_j p_j(x))].
   \]
   But in **Section 3.3** on **Page 5**, \(\bar f_i\) is re-described as “the normalized score assigned to the token of expert \(i\) in the first \(k\) routes,” which is not the same object. That is not a cosmetic problem. It changes whether RSL depends on hard top-1 counts, top-\(k\) counts, or soft assignments. Since the auxiliary term is central to the method, this ambiguity matters for both reproducibility and interpretation. The paper should define one exact quantity and stick with it.

3. **The gradient derivation for RSL is too hand-wavy relative to the claims made from it.**  
   In **Equations (7) to (9)** on **Page 5**, the paper derives
   \[
   \nabla_{p_i(x)}\mathcal L_{\mathrm{RSL}} = \alpha \cdot \frac{\partial \bar p_i}{\partial p_i(x)} \cdot \bar f_i + \lambda(\log p_i(x)+1-\mu).
   \]
   This omits the dependence of \(\bar f_i\) on \(p_i(x)\), unless one is already assuming a surrogate, in which case the paper should say so in the main text rather than only later in the appendix. Moreover, the route from this expression to the strong claims that RSL “encourages high variance,” “improves robustness,” and “provides strong convexity and well-conditioned optimization” is too fast. The derivation as written is not enough to support those claims for the actual neural router parameters. It is only about distributions \(p(x)\) treated as optimization variables, which is a much easier and less realistic problem.

4. **The theory feels disconnected from the implemented method, and key assumptions are doing most of the work.**  
   The appendix theory is not required for validity, but the main paper leans on it quite heavily. In **A.1**, the convergence result assumes a smoothed surrogate and explicitly assumes the auxiliary composite term is convex and \(L\)-smooth on the product simplex. That is a very strong assumption, and it sidesteps the actual nonconvex optimization over router network parameters. In other words, the paper proves properties of an idealized objective over routing distributions, not of the model actually trained. This matters because the main text on **Page 5** presents the entropy term as if it directly yields stable optimization and generalization for the practical method. That interpretation is much stronger than what is actually justified.

5. **The experimental comparisons are broad, but not always controlled enough to isolate the claimed source of gains.**  
   In **Table 2** on **Page 7**, LoRA-Mixer is compared against LoRAHub, MoLE, MixLoRA, and a “LoRA” baseline, but it is hard to tell whether the comparison cleanly isolates routing location, routing loss, and parameter budget at the same time. For example, the paper repeatedly emphasizes parameter efficiency, but the main results table does not report trainable parameters or inference costs alongside accuracy. Those numbers are only pushed to the appendix. Since the abstract makes a parameter-efficiency claim, the main comparison table should include parameter counts directly. Otherwise, a reader cannot tell whether gains come from the routing design or simply from allocating adaptation capacity differently.

6. **Some numerical improvements are inconsistent or too small to support strong wording, and there is little statistical treatment.**  
   The paper says all experiments are run three times on **Page 6**, but no standard deviations or confidence intervals are reported in any main table. That is a problem because several gains are very small. In **Table 2** on **Page 7**, for Mistral-7B on GSM8K, LoRA-Mixer gets 46.48 while plain LoRA gets 46.67, so the proposed method is actually worse there. On Falcon-Mamba ARC-C, LoRA-Mixer is 77.19 while plain LoRA is 76.51, a gain of 0.68, which may or may not be meaningful without error bars. The paper’s tone often reads as if the method strictly dominates all alternatives, but the tables show a more mixed picture. If the evidence is based on small deltas, variance reporting becomes necessary.

7. **The “plug-and-play with public LoRAs” claim is interesting, but the main paper does not probe failure modes or compatibility constraints.**  
   The discussion on **Page 4** and **Section 4.3** on **Page 8** makes this sound easy, but in practice adapter composition is sensitive to target modules, rank choices, tokenizer/base-model alignment, and training recipes. **Table 3** on **Page 7** reports promising Flan-T5 results, but this is only one base model and five LoRAs, all within a fairly controlled setup. There is no analysis of when plug-and-play fails, whether adapters trained on mismatched module sets can be composed, or how much normalization/calibration is required. For a paper selling modular reuse, these practical constraints matter a lot.

8. **The transfer claim is intriguing but currently under-validated.**  
   **Table 5** on **Page 7** transfers Mistral-trained parameters to LLaMA3-8B “without any fine-tuning and adaptation.” This is a neat experiment, but the evidence is thin: only three datasets are reported, one of them degrades substantially on ARC-E, and the transfer is between closely aligned architectures. The paper then states on **Page 8** that the learned routing is “extremely robust and transferable,” which feels overstated based on this narrow experiment. I would treat this as an interesting preliminary observation, not a demonstrated property.

9. **The figure-based routing analysis is suggestive, but still too qualitative for the strength of the claims.**  
   **Figure 3** on **Page 8** shows average load per expert around 15% to 18%, which supports the narrow claim that catastrophic collapse is avoided. But balanced average load is not the same as useful specialization. Likewise, **Figure 4** on **Page 9** visually suggests that RSL gives higher activation to domain-relevant experts, but the figure is qualitative and lacks exact definitions of the experts, normalization protocol, and whether the plotted values are averaged over tokens, samples, or datasets. Since routing specialization is the centerpiece of the paper, this analysis should be more quantitative, for example with expert-task mutual information, entropy statistics, or task-conditioned activation matrices with exact scales and confidence intervals.

10. **Presentation quality is below ICLR expectations for a method paper with equations.**  
   There are many writing and editing issues in the main paper. A few examples: duplicated caption text for **Table 2** on **Page 7**; inconsistent naming of the loss as “Routing Specialization Loss,” “Router Specialization Balancing Loss,” and “Routing Specialization Balance Loss”; unclear phrases such as “fusion expert” in **Section 3.2**; and a badly corrupted references section on **Pages 10 to 13** with repeated, seemingly irrelevant entries. There is also a dangling “Table ??” reference in **A.14**. None of these alone kills the paper, but together they make the work feel under-polished and reduce confidence that the method details are as solid as they should be.

## Questions
1. Please state the exact forward computation used in the main model, replacing the abstract notation in **Equation (4)** with a fully explicit formula. In particular, what is the exact definition of \(\mathcal F_{\text{route}}\), how is top-\(k\) applied, are the selected weights renormalized, and how are gradients handled during training?

2. What is the precise definition of \(\bar f_i\) used in **Equation (5)**? The paper gives at least two different descriptions, top-1 empirical usage in **Equation (3)** and something closer to normalized top-\(k\) score mass in **Section 3.3**. This should be clarified unambiguously.

3. Can the authors provide standard deviations or confidence intervals for the main tables, especially **Table 2**, **Table 3**, **Table 7**, **Table 8**, and **Table 9**? Several reported gains are small enough that variance could change the interpretation materially.

4. To better isolate the architectural claim, can the authors add or clarify a comparison between:  
   (a) projection-layer LoRA mixture with standard auxiliary loss,  
   (b) projection-layer LoRA mixture with RSL,  
   (c) FFN-style or branch-style mixture with the same RSL,  
   all under matched parameter budgets?  
   Right now the method combines a routing-location change and a routing-loss change, making attribution difficult.

5. For the plug-and-play setting, what compatibility conditions are required among public LoRAs? Must they share the same rank, target modules, scaling conventions, and base model family? A short negative-case discussion would increase confidence in the practical claims.

6. The theory would be easier to trust if the main text clearly stated that the convexity and stability results apply to a surrogate optimization over routing distributions, not to the full neural training problem. Can the authors sharpen that distinction and tone down the stronger causal language if needed?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work focuses on model adaptation and routing for public benchmarks. Standard downstream deployment concerns for LLMs remain, but the submission does not introduce a distinct ethical risk that requires specialized ethics review.

## Soundness Rating
2: fair. The paper has a plausible method and a large empirical sweep, but the main mathematical formulation is underspecified, the theory relies on strong surrogate assumptions, and several core claims are supported less cleanly than the text suggests.

## Presentation Rating
2: fair. The central idea is understandable, and **Figure 1** and **Figure 2** help, but the paper suffers from inconsistent notation, duplicated table text, ambiguous loss definitions, and a messy reference section.

## Contribution Rating
3: good. Despite the issues, the paper tackles a useful problem, offers a meaningful design variation for modular LoRA composition, and presents broad empirical evidence that the approach is worth the community’s attention.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I lean slightly positive because the problem is relevant, the architectural idea is sensible, and the empirical results are broad and mostly favorable. That said, this is not a comfortable accept. The paper needs sharper method specification, tighter causal attribution in experiments, and much cleaner exposition.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I carefully checked the main equations, figures, and result tables, and I am familiar with the surrounding LoRA/MoE literature, but some implementation details remain ambiguous in the paper itself.