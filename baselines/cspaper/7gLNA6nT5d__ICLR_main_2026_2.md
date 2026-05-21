---
job_id: ae9a8c49-8e98-4bee-bcf8-5f4a94ef4375
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 7gLNA6nT5d.pdf
paper: Formatting Instructions for ICLR 2026 Conference Submissions
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically reinforcement learning, in-context learning, and transformer-based representation/sequence modeling.

## Minimum Quality
Pass ✅. The submission contains the expected research-paper components, including Abstract, Introduction, Method, experimental setup, quantitative results, Related Work, and Conclusion. While there are notable issues in rigor, positioning, and clarity, they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-directed text, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies whether explicitly inserting n-gram induction heads into transformers can improve in-context reinforcement learning, using Algorithm Distillation (AD) as the main baseline. The authors modify the transformer with an n-gram attention layer, adapt the mechanism to pixel observations via vector quantization, and evaluate on Dark Room, Key-to-Door, and Miniworld variants. The main claims are improved data efficiency and reduced hyperparameter sensitivity relative to AD.

## Strengths
The paper tackles a relevant problem. In-context RL is appealing but notoriously data-hungry and unstable, and the attempt to inject a mechanistic inductive bias, motivated by induction-head literature, is a reasonable direction.

The empirical story is fairly consistent across several environments. In particular, **Figure 2** on Page 3 and **Figure 4** on Page 5 both support the paper’s central qualitative claim that the proposed model tends to reach stronger performance with fewer hyperparameter assignments than the vanilla AD baseline under the authors’ chosen protocol. Even though I have concerns about interpretation, the trend itself is visible and is not confined to a single benchmark.

I also appreciated that the paper tries to move beyond tiny symbolic settings. The extension to pixel observations via quantization is a practical addition, and **Figure 5** on Page 6 suggests the method is not restricted to discrete-state grid worlds. This makes the submission more interesting than a purely toy-gridworld paper.

The paper includes some effort to check whether the added n-gram machinery introduces major hyperparameter burden or can catastrophically damage a baseline. **Table 1(a,b,c)** on Page 9 is useful in that regard. In particular, the relatively similar EMP values across n-gram lengths and insertion positions are at least suggestive that the method may not be extremely brittle to those specific design choices, and the “permuted mask” comparison is a sensible sanity check to include.

The writing is generally understandable at the high level. The motivation, benchmark descriptions, and intended claims are easy to follow even when some technical details are underspecified.

## Weaknesses
I have several substantial concerns. Some are fixable with better exposition or additional experiments, but in the current form they materially weaken the paper’s scientific value.

1. **The main empirical comparisons are not clean enough to support the headline efficiency claims.**  
   The paper repeatedly claims substantially better data efficiency than AD, including the “27x less data” statement on Page 2 and again in Section 4.2 on Page 7. However, the comparison is not apples-to-apples. The paper compares against numbers reported in Laskin et al. for one setup, while the current submission uses its own data-generation pipeline, altered task/history ratios, a different hyperparameter search protocol, and in image settings even an oracle-plus-noise data collection procedure (Page 6, Section 3.3). That makes the “27x” figure much less definitive than the prose suggests. This matters because it is presented as a core contribution, not a side observation. If the data source, task distribution, and collection procedure change, then transition-count comparisons alone do not establish superior sample efficiency of the method.

2. **The evaluation protocol conflates model quality with hyperparameter search budget, and this is not handled carefully enough.**  
   Section 3.2 on Page 5 adopts Expected Maximum Performance (EMP) over random hyperparameter search as the main reporting mechanism. That is acceptable as one lens, but the paper then uses it to argue that the method is easier to train and better performing. Those are not the same claim. A method can look better under EMP simply because it is less variable under a particular sweep distribution, not because its best achievable performance or average performance is stronger.  
   This issue is visible in **Figure 2** and **Figure 4**. Both figures are curves over “# hyperparameter assignments”, which primarily evaluate success under search budget, not pure algorithmic capability. The paper should also report fixed-hyperparameter comparisons, or at least distributions over final performance under matched sweep spaces, to disentangle robustness from raw performance. Without that, the central interpretation remains somewhat slippery.

3. **The hyperparameter search itself may not be a fair comparison between baseline and proposed method.**  
   The paper states in Section 4.1 on Page 7 that it performs random search over “core transformer hyperparameters that do not change the parameter count,” but Appendix C / Table 2 shows search spaces that include `ngram head pos` and `ngram max` for the proposed method, while the baseline obviously does not have these parameters. More importantly, the search distribution itself may favor one method over the other if the baseline is more sensitive to some parameters, or if the proposed model effectively gets access to a broader favorable region. The paper needs to spell out whether the shared hyperparameters were sampled from identical distributions across methods, whether the same number of total trials was used, and whether the baseline had any compensating architecture-specific tuning. This matters because the central result is precisely about hyperparameter sensitivity.

4. **The mathematical specification of the n-gram mechanism is too underspecified for a paper whose contribution is architectural.**  
   In Section 2.2, **Equation (1)** defines  
   \[
   A^{(n)}_{ij} \propto \mathbb{1}\!\left[\bigwedge_{k=1}^{n} x_{i-k}=x_{j-k-1}\right].
   \]
   There are several issues here. First, the indexing is not explained carefully: why is the right-hand side shifted by \(j-k-1\) rather than \(j-k\)? Is this inherited exactly from [2], or adapted for RL tokenization? Second, the proportionality sign leaves normalization unspecified. Is \(A^{(n)}\) row-normalized, column-normalized, or left as a binary mask? Third, the definition of the tokens \(x_i\) is ambiguous once the RL sequence interleaves state, action, and reward tokens. Section 2.3 says the authors tried matching either full transitions \((a_{i-1}, r_{i-1}, s_i)\) or states only, but the connection between that choice and **Equation (1)** is never formalized.  
   This matters because the exact matching object is the core of the method. Right now, the implementation-critical part of the model is described more like a sketch than a reproducible specification.

5. **The layer equations omit important details and create ambiguity about how the module interacts with the transformer.**  
   **Equation (2)** and **Equation (3)** on Pages 3 to 4 define
   \[
   \mathrm{NGH}^{n}(h^l)=W_1 h^l + W_2 (A^{(n)})^\top h^l
   \]
   and
   \[
   \mathrm{NGL}^{n}(h^l)=h^l+\mathrm{MLP}\!\left[\mathrm{NGH}^{n}(h^l)\right].
   \]
   But there is no discussion of dimensionalities, whether \(A^{(n)}\) is detached or differentiable through the matching procedure, how this replaces or complements standard self-attention, and whether masking for causality is enforced inside \(A^{(n)}\). The text says the n-gram layer is “used as one of the transformer layers” and “closely resembles a traditional transformer layer,” but it is not clear if a normal attention block is removed, parallelized, or stacked in addition. Since this is the central mechanism, the lack of architectural precision is a real problem, not a cosmetic one.

6. **The visual-observation matching mechanism is brittle and insufficiently validated.**  
   Section 2.3 on Page 4 says that each image is mapped into a \(4 \times 4\) matrix of VQ indices and a match is counted “only if all the indices in the matrix are equal.” That is an extremely hard equality criterion. In visual RL, even observations from the same underlying state often vary due to viewpoint, rendering, or minor nuisance factors. The paper motivates VQ as a way to ignore slight visual differences, but the all-cells-equal rule seems to reintroduce a very strict exact-match requirement in the discrete latent space.  
   This matters because the claimed success in Miniworld rests on this mechanism. Yet the paper provides no analysis of match rates, collision rates, quantization error, or how often semantically same states map to the same code grid. The “permuted mask” result in **Table 1(c)** is useful, but it does not validate that the actual mask is semantically meaningful, only that a broken mask does not outperform baseline.

7. **Several claims are stronger than what the evidence actually supports.**  
   For example, the abstract says the approach “considerably reduced the amount of data required for generalization and eased the training process by making models less sensitive to hyperparameters.” The evidence for “less sensitive” is indirect and tied to the EMP-over-random-search protocol. The evidence for “reduced the amount of data required” is strongest only in a narrow set of toy environments and with a somewhat loose cross-paper comparison. Likewise, the conclusion on Page 9 states that n-gram heads “sufficiently ease training” of ICRL algorithms in general, which is broader than what three small benchmark families can establish.  
   I do not mind ambitious claims, but the current wording overshoots the evidence.

8. **The empirical scope is still quite limited for the breadth of the claims.**  
   The paper itself acknowledges in the conclusion that more comprehensive environments are future work. That is fair, but then the framing should be more modest. Dark Room and Key-to-Door are standard stress tests for adaptation and memory, but they are still simple environments with short horizons and highly repetitive structure, precisely the setting where explicit n-gram matching may shine. The Miniworld tasks are a useful step, yet they remain stylized versions of the same underlying problems. This matters because the method may exploit repeated local sequence motifs that are abundant here but much less informative in richer control problems.

9. **The paper does not adequately separate the effect of architectural bias from the effect of representation choices and data pipeline choices.**  
   In the image setting, the method’s performance depends not just on the n-gram layer, but on a pretrained VQ encoder-decoder, the codebook discretization, and the exact equality rule for matching. In the grid setting, it also depends on whether matching is done on states or on full \((s,a,r)\)-style transitions. In **Figure 2** on Page 3, the “states” and “\([s,a,r]\)” variants already show noticeable differences, which suggests the design choice is important. Yet the paper does not systematically analyze when one matching scheme should be preferred, or how much of the gain is attributable to that choice versus the existence of the n-gram layer itself.

10. **Presentation is decent at the narrative level, but there are many local clarity issues and some sloppiness.**  
   There are multiple grammatical mistakes and notation inconsistencies, for example the sequence in Section 2.3 is written as \((s_0,a_0,r_0,\ldots,s_n,a_n,r_0)\), where the final reward index looks like a typo; “Miniworld” and “Minigrid” are both used in Section 4.3 on Page 7; and some claims point to appendices for crucial justification. These are not fatal by themselves, but they add friction and make it harder to trust the exact technical story.

11. **The ablation evidence in Table 1 is too thin to justify the conclusion that the extra hyperparameters are essentially harmless.**  
   On Page 8, Section 4.4 states that there is “no significant difference” across n-gram lengths and layer positions. But **Table 1(a,b)** reports only final EMP values in Miniworld-Dark, with no statistical testing, no number of runs, and no evidence that this generalizes to other tasks. Also, the differences are not always negligible relative to the reported deviations, for example \(0.76 \pm 0.05\) versus \(0.69 \pm 0.03\). That may or may not be meaningful, but the paper should not so quickly conclude “little to no overhead in hyperparameter search.”

12. **The paper’s positioning relative to prior work is a bit too self-congratulatory given how direct the borrowing is.**  
   The method is, by the authors’ own description, integrating the n-gram layer of Akyürek et al. into an AD-style in-context RL pipeline. That can still be publishable if the empirical study is especially strong or reveals new insights. But then the paper needs to be more precise about what is genuinely learned here beyond “this inductive bias helps in these tasks.” Right now, the mechanistic explanation remains speculative, and the empirical evidence, while suggestive, is not strong enough to fully carry the paper.

## Questions
1. The most important clarification I would like is a **precise formal definition of the matching tokens \(x_i\)** used in **Equation (1)** for RL sequences. Are states, actions, and rewards separate tokens in the transformer? If so, how exactly is \(A^{(n)}\) computed over the mixed sequence? If instead matching is done over grouped transition-level units, please rewrite the equations accordingly.

2. Please clarify the **normalization and masking of \(A^{(n)}\)**. Is \(A^{(n)}\) binary, row-stochastic, column-stochastic, or scaled in some other way? How do you ensure causality? This is central for reproducibility.

3. Can the authors provide a **cleaner data-efficiency comparison under a matched setup**, rather than relying on transition-count comparison to a previously reported AD number? For example, training both baseline and proposed method on the same datasets, with matched task distributions and matched history counts, and then reporting performance as a function of total transitions would substantially increase my confidence.

4. Since EMP over random search is central to the paper, can the authors also report **best-of-sweep** and **mean-over-sweep** metrics, or performance under a fixed common hyperparameter configuration? That would help separate “easier to tune” from “fundamentally better.”

5. For the image setting, can the authors provide **diagnostics of the VQ matching quality**, such as: fraction of repeated observations that produce exact latent-grid matches, whether nearby views of the same state collide, and some qualitative examples of matched vs mismatched image pairs? This would make the Miniworld results much more convincing.

6. In **Figure 2**, the “states” and “\([s,a,r]\)” variants behave differently. Under what conditions should one expect state-only matching to be better than transition-level matching? A more principled explanation here could strengthen the paper beyond pure benchmarking.

7. Please specify whether the n-gram layer **replaces a self-attention block or is inserted alongside one**, and whether parameter counts are matched to the baseline. This matters for interpreting the gains.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work studies RL algorithms in simulated environments and does not involve human subjects, sensitive personal data, or obviously harmful deployment claims.

## Soundness Rating
2: fair. The empirical results are suggestive, but several core claims are only partially supported, the comparisons are not fully controlled, and the architectural specification is too underspecified for high confidence.

## Presentation Rating
2: fair. The paper is readable at a high level, but important equations and implementation details are ambiguous, and there are several notation and exposition issues.

## Contribution Rating
2: fair. The idea of porting n-gram induction heads into in-context RL is interesting, but the contribution feels incremental relative to prior induction-head work, and the current evidence is not strong enough to establish a broad advance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a plausible idea and some encouraging empirical trends, especially in **Figures 2, 4, and 5**, but the current version overclaims relative to the evidence. The main issues are the lack of a clean apples-to-apples efficiency comparison, the heavy reliance on EMP-over-search as the primary evaluation lens, and insufficiently precise specification of the core n-gram mechanism in **Equations (1)-(3)**. I can imagine a stronger revision becoming competitive, but this version falls short of ICLR main-track standards for me.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. The paper is in an area I know well, and I checked the core experimental and mathematical details carefully, but some ambiguities in the submission prevent absolute certainty.