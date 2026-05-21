---
job_id: 192a4736-6a89-4393-895b-f1933f2e43ad
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: vGkXf8nvt9.pdf
paper: Forget-to-Focus: Can Unlearning Improve Domain Specialization in LLMs?
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies transfer learning/domain adaptation for LLMs through a machine unlearning procedure, with optimization and representation-analysis components.

## Minimum Quality
Pass ✅. The submission contains the core ingredients of a research paper, namely abstract, introduction, method, experiments/results, and conclusion; related work is integrated into the introduction rather than separated as its own section. While I have substantial concerns about rigor, theory-to-practice alignment, and experimental design, these are review-level weaknesses rather than desk-rejection-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions aimed at automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies whether a targeted unlearning step before domain adaptation can improve specialization of pretrained LLMs. The proposed Forget-to-Focus (F2F) protocol first applies unlearning on a forget set, optionally stabilized with a retain set, and then fine-tunes on a target domain, with experiments across coding, medical QA, and mathematics on models ranging from 0.6B to 72B parameters. The paper also presents a simplified theoretical argument based on a convex surrogate and analyzes representation changes using CKA and SVCCA.

## Strengths
The paper asks an interesting question that is worth studying: can unlearning be repurposed from privacy/compliance into a pre-adaptation intervention for reducing negative transfer? That framing is useful and broader than a narrow algorithm paper.

The empirical scope in the main paper is reasonably broad. The authors evaluate across three target domains, several model families, and multiple adaptation baselines. This is better than the common pattern of making a claim from one model and one benchmark only.

Table 1 on Page 7 is the strongest piece of evidence in the paper. In several cases, the proposed recipe of unlearning followed by SFT does improve over standard SFT, DAPT, and LoRA, sometimes by large margins, for example on Qwen 0.6B and LLaMA 8B for HumanEval and MBPP. Even though I have concerns about variance and fairness of some comparisons, the table does suggest that the phenomenon is real in at least some settings.

Table 3 on Page 9 is also a useful addition because it goes beyond pure headline numbers and shows sensitivity to the forget-set construction. In particular, the comparison between BC-Select, BC-Mixed, and BC-Cosine is important because the entire premise of F2F depends on identifying data that should be forgotten. I appreciate that the paper at least attempts to probe this axis instead of treating forget-set selection as a trivial detail.

Figure 2 on Page 5 is helpful as an intuition-building diagnostic. The t-SNE visualization of BC-Mixed does support the claim that the forget-set construction includes separable general and domain-related regions, which is relevant to the paper’s argument that domain contamination matters. I do not think this figure proves “no leakage,” but it is still a useful sanity check.

The paper does more than just report accuracy. The representation-analysis section, especially Figure 4 and Figure 5, tries to examine whether F2F changes internal geometry differently from standard tuning. Even though the causal interpretation is overstated, this is still a constructive attempt to understand mechanism rather than only leaderboard movement.

The main idea is operationally simple. The update in Equation 3 is easy to implement, and the protocol is modular enough that practitioners could try it with existing unlearning recipes.

## Weaknesses
1. **The central theoretical claim is much stronger than what the theory actually supports.**  
   Equation 1 on Page 3 states the core desired implication,
   \[
   \|\tilde{\theta}_0-\theta^\star\| < \|\theta_0-\theta^\star\| \Rightarrow L_D(\mathrm{FINETUNE}(\tilde{\theta}_0)) < L_D(\mathrm{FINETUNE}(\theta_0)).
   \]
   This is presented as the conceptual basis of the method, but it is not justified for the actual non-convex LLM setting considered in the paper. The subsequent proposition and corollary only analyze a highly simplified strongly convex surrogate with an orthogonal decomposition \(\mathbb{R}^p=\mathcal V\oplus\mathcal U\), assuming \(\theta^\star\in\mathcal V\), strong convexity of \(L_F\) along \(\mathcal U\), and bounded retain gradients. Those are very restrictive assumptions, and the paper does not explain why they should hold even approximately in transformer parameter space. As written, the theory functions more like a motivational cartoon than evidence for the claimed optimization mechanism. This matters because the paper repeatedly uses the theory to argue that larger forget-to-retain ratios should improve downstream risk, yet this relationship is not established for the real method.

2. **There are mathematical and notational issues in the formulation that make the method harder to verify than it should be.**  
   On Page 3, Equation 2 defines
   \[
   \tilde{\theta}_0 = \arg\min_\theta \frac{1}{A}\sum_{u=1}^A \left[-\lambda \ell_F^{(u)}(\theta) + \sigma \ell_R^{(u)}(\theta)\right],
   \]
   but \(\ell_F^{(u)}\) and \(\ell_R^{(u)}\) are never clearly specified as token-level NLL, sequence-level loss, or minibatch-averaged objectives. This is not a cosmetic issue, because in language modeling the precise reduction and normalization matter when mixing ascent and descent terms. Likewise, the paper says Equation 2 uses “gradient-accumulation averaging over \(A\) micro-steps,” but the operational algorithm immediately afterward switches to minibatch gradients \(g_F=\nabla \ell(B_F;\theta)\), \(g_R=\nabla \ell(B_R;\theta)\) without specifying whether the same normalization is used in practice. There is also inconsistency between the generalized objective on Page 3 and the variant-specific objectives on Page 4, especially GA+KL and NPO, which are mentioned as realizing Equation 2 “in practice,” even though NPO is not a simple instantiation of the same ascent/descent objective. The paper needs a cleaner unified notation and explicit training losses.

3. **The forget-set construction is the crux of the method, but the paper treats it too casually, and the evidence for correctness is weak.**  
   The paper’s gains depend heavily on having a forget set that contains “irrelevant” pretraining knowledge. Yet on Page 5, the forget sets are built from BookCorpus subsets plus manually excluded or automatically filtered examples, and the retain set is “a small subset of the fine-tuning data.” This is a very favorable setup that may substantially bake in the answer. If the retain set comes from the target-domain training set, then the unlearning stage is not purely domain-agnostic preparation, it is already using task/domain supervision to shape the model. That may be perfectly legitimate, but it changes the interpretation of what is being shown. Figure 2 is used to argue “clear boundary” and “no domain leakage,” but a 2D t-SNE separation of MiniLM embeddings is far too weak to support that conclusion. t-SNE can produce visually separated clusters even when neighborhoods overlap in the original space, and the figure only addresses BC-Mixed for one embedding model, not the broader forget-set design used throughout the paper. This matters because if forget/retain partition quality is fragile, then the practical applicability of F2F becomes much narrower than the paper suggests.

4. **The experimental comparisons are not always fair across methods and scales.**  
   The setup on Pages 5 and 6 uses different training regimes across models: Qwen 0.6B gets 8 epochs, most other models get 1 epoch; Qwen 72B uses QLoRA, 4-bit quantization, and only 50% of the original dataset. Some baselines are full SFT, others are LoRA-based, and in Table 1 the proposed method is often “unlearning + SFT,” whereas some baseline rows are just LoRA or CurlLoRA. The paper then makes broad claims that F2F outperforms standard fine-tuning and parameter-efficient baselines, but the comparison budget and adaptation recipe are not consistently matched. This especially matters for the 72B results, where the protocol differs materially from smaller models. Without more careful control of training budget, wall-clock, token budget, and trainable parameters, it is difficult to isolate whether gains come from the unlearning idea itself or from asymmetries in adaptation setup.

5. **Variance reporting in the main paper is missing, yet many conclusions are drawn from small differences.**  
   Tables 1, 2, and 3 report single numbers without confidence intervals or standard deviations. Some reported improvements are large and likely robust, but many others are modest, for example a few tenths to a couple of points. The appendix includes a three-seed analysis, but the review outcome should be assessable from the main paper, and the main paper currently does not let the reader distinguish stable gains from run-to-run noise. This matters even more because unlearning is known to be unstable, and Table 1 itself already shows catastrophic drops for some models in the intermediate unlearning stage, such as Gemma 2B and LLaMA 13B. A method that can both help dramatically and collapse dramatically deserves stronger statistical characterization in the main text.

6. **Some empirical claims are overstated relative to what the figures actually show.**  
   The discussion around Figure 4 on Page 8 says that F2F “consistently pushes representations further from the unlearned model.” But Figure 4 mainly plots linear CKA curves relative to compared states, and visually the message is simply that both tuned and F2F models have low similarity in several settings. Low CKA means drift, not necessarily that the drift is toward a more domain-useful representation or that it reallocates capacity. Similarly, Figure 5 on Page 10 provides SVCCA heatmaps, but the interpretation remains largely qualitative and descriptive. The paper repeatedly jumps from “representation changed more” to “negative transfer was reduced,” which is a much stronger causal statement than the evidence supports. Representation diagnostics are useful, but they do not validate the mechanism on their own.

7. **Table 2 is underleveraged and somewhat disconnected from the main F2F claim.**  
   Table 2 on Page 7 compares SFT, LoRA, CurlLoRA, and DAPT in the medical domain, but F2F is not included in the table itself even though the subsection is titled “F2F w/ Fine-tuning Variants.” This makes the section harder to parse. If the purpose is to study interaction between unlearning and fine-tuning variants, the table should explicitly include the corresponding F2F versions of these methods, not just the plain adaptation baselines. As written, the text discusses conclusions about structured fine-tuning and larger models, but the table does not fully support the framing.

8. **The paper does not quantify the compute and efficiency trade-off of adding an explicit unlearning stage in the main paper.**  
   F2F introduces a non-trivial extra phase before fine-tuning. For a method positioned as practical and modular, one would expect clear reporting of unlearning cost relative to baseline tuning, perhaps in GPU-hours, tokens processed, or additional optimization steps. Instead, the main paper gives step counts and generic hardware information, while the cost discussion is pushed to the appendix. This omission matters because a method that yields modest gains at large extra cost may be less attractive than a slightly weaker but simpler baseline such as DAPT or standard SFT.

9. **The literature positioning is incomplete for a paper making strong mechanistic claims about unlearning and representation change.**  
   The paper cites several machine-unlearning works, but it does not engage with more recent work on representation-level or layer-wise unlearning analysis, which is especially relevant given the paper’s CKA/SVCCA-based claims about internal geometry. This weakens the novelty positioning around the analysis component and leaves the reader unsure how much of the observed behavior is already known in the unlearning literature.

10. **The writing is understandable overall, but there are many imprecise or inflated statements that hurt scientific clarity.**  
   Examples include “Figure 2 demonstrates the clear boundary ... ensuring no domain leakage” on Page 5, and repeated uses of words like “proves” or “direct evidence” in contexts where the evidence is correlational. There are also several grammar issues and presentation inconsistencies, such as “with different architecture” vs. “architectures,” inconsistent capitalization of LoRA/CurlLoRA, and table labels that are sometimes confusing, for example the merged-looking “BC-CosineBC-Mixed” entries in Table 3 on Page 9. None of this is fatal by itself, but it contributes to a sense that the paper is reaching beyond what it has rigorously established.

## Questions
1. The main practical concern is forget-set construction. Can the authors provide a cleaner protocol that does **not** use a retain set drawn from the target-domain training data, or at least disentangle how much of the gain comes from target-domain exposure during unlearning versus the actual forgetting operation? An ablation with retain sets from a generic corpus, from the target domain, and with \(\sigma=0\) would be helpful.

2. Please clarify the exact loss implementation behind Equations 2 and 3. Is \(\ell\) token-level next-token NLL averaged over all tokens in the batch, sequence-averaged NLL, or something else? How are the ascent and descent terms normalized relative to one another when forget and retain batches have different lengths or token counts?

3. Can the authors provide a strictly budget-matched comparison in the main paper, at least for one representative model, where baseline SFT and F2F use the same total number of optimization steps and the same effective number of trainable parameters? Right now, the extra unlearning phase makes it hard to know whether F2F is truly better per unit compute.

4. Table 2 is hard to interpret in its current form because it omits F2F variants while the subsection discusses them. Can the authors add rows such as F2F+SFT, F2F+LoRA, F2F+DAPT, and F2F+CurlLoRA under identical settings?

5. The convex surrogate theory would be more convincing if it were tied to empirical observables. For example, can the authors test whether increasing \(\lambda/\sigma\) monotonically reduces some proxy for “irrelevant subspace magnitude” or improves downstream convergence as suggested by the corollary on Page 4? Right now the link between theory and experiments is mostly narrative.

6. Figure 2 uses t-SNE of MiniLM embeddings to argue limited overlap. Can the authors support this more rigorously with quantitative overlap metrics, such as nearest-neighbor contamination rates, classifier distinguishability, or cosine-similarity distributions between forget and target-domain corpora?

7. Several reported gains are small while others are large. Please add multi-seed results with standard deviations for the main tables, not only supplementary analysis, especially for Table 1 and the forget-set comparisons in Table 3.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper repurposes machine unlearning as a performance-enhancement tool rather than a privacy tool. That direction is not inherently problematic, but it does create a risk of overclaiming “unlearning” in settings where the intervention is really a targeted reweighting or suppression of model behavior rather than verified deletion of knowledge. Since the paper studies medical QA as one of its domains, this matters more than usual. The appendix mentions improved calibration, which is positive, but the main paper should more clearly separate performance gains from safety guarantees, and avoid implying that targeted forgetting automatically yields more reliable medical behavior.

## Soundness Rating
2: fair. The empirical phenomenon is plausible and sometimes compelling, but the methodological controls, statistical reporting, and theory-to-practice linkage are not strong enough for a higher score.

## Presentation Rating
3: good. The high-level idea is understandable and the paper is reasonably organized, but there are notable clarity issues, overstatements, and some confusing tables/notations.

## Contribution Rating
2: fair. The framing of unlearning as a preparatory specialization tool is interesting, and some results are promising, but the paper does not yet establish the idea with the rigor or precision needed for a stronger contribution rating.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a real signal here, and some of the coding results are genuinely interesting. Still, the current version overstates what its theory and analyses show, under-specifies the actual training objective, and relies heavily on favorable forget/retain construction without fully confronting how fragile that assumption may be. This feels like a promising paper that is not yet pinned down tightly enough for ICLR acceptance.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with the relevant unlearning / LLM adaptation literature and checked the core mathematical and experimental claims carefully.