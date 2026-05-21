---
job_id: e787c691-7ed9-4747-b865-73b61463d282
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ZMzha5gbnF.pdf
paper: Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically generative models, language modeling, and ML safety for diffusion language models.

## Minimum Quality
Pass ✅. The submission contains all core components expected of a research paper, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion, and it provides enough technical and empirical material to evaluate the main claims.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-directed instructions, or other suspicious manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies a safety failure mode specific to masked diffusion language models, which the authors call the priming vulnerability: if an affirmative token appears in an intermediate denoising state for a harmful query, later denoising can be steered toward a harmful answer. The paper analyzes this phenomenon under both intervention and non-intervention threat models, introduces a first-step surrogate objective for GCG-style attacks, and proposes Recovery Alignment (RA), which trains the model to recover from contaminated intermediate states back to safe responses.

## Strengths
The paper asks a timely and relevant question. Safety work for autoregressive LMs is already extensive, but diffusion language models have a different inference mechanism, so it is useful to test whether familiar safety intuitions actually transfer. The paper identifies a concrete mechanism tied to iterative denoising rather than just reporting generic jailbreak numbers.

I found the empirical phenomenon itself convincing. **Figure 2** on **Page 4** is one of the stronger parts of the paper: it cleanly shows that ASR increases with the intervention step, and more importantly, that even an intervention at \(t_{\mathrm{inter}}=1\) materially changes behavior. That plot supports the paper’s central claim that the vulnerability is not merely a late-step artifact. The paper also does a good job connecting this figure to the intuition that a single early anchor can bias the later denoising trajectory.

The proposed defense is well matched to the diagnosed failure mode. If the problem is that standard alignment only teaches safe generation from \(r_0\), then training from contaminated intermediate states is a natural and technically coherent response. This is also reflected in the ablation design. In **Table 2** on **Page 8**, the comparison between RA and **RA w/o inter** is particularly important, because it isolates the effect of training on contaminated states rather than attributing gains to generic RLHF-style tuning. For both LLaDA variants, the drop in ASR under anchoring and First-Step GCG is large and consistent, which strengthens the causal story the paper wants to tell.

The experimental section is fairly broad for a main paper. The authors evaluate three MDLMs, several attack types, both intervention-based and conversational jailbreaks, and also report general-capability results on eleven benchmarks. **Table 3** on **Page 8** suggests that the benefit of RA is not confined to the exact anchoring attack used to motivate the method, and **Table 4** on **Page 9** shows that average utility does not collapse after alignment. That combination makes the paper more useful than a narrow attack note.

The ablations are also informative rather than perfunctory. **Figure 3(a)** on **Page 9** shows that robustness improves with larger \(t_{\max}\), but not without cost, and **Figure 3(b)** provides evidence that linear scheduling is better than uniform or constant scheduling. These figures help clarify why the proposed curriculum is not just an arbitrary training detail.

Finally, the paper is generally easy to follow. The high-level story around **Figure 1** on **Pages 1-2** is intuitive and does real explanatory work: panel (a) explains MDLM denoising, panel (b) illustrates the vulnerability, and panel (c) motivates the training intervention. For a paper introducing a model-specific safety concept, that framing matters.

## Weaknesses
My main concern is that the paper’s strongest theoretical statement is not as solid as the text suggests. In **Theorem 4.1** on **Page 5**, the lower bound in **Equation (3)** depends on a monotonicity assumption,
\[
\log \pi_{\theta}(\tilde{\mathbf r}_{t+1}=\mathbf r \mid \mathbf q,\mathbf r_t) \ge \log \pi_{\theta}(\tilde{\mathbf r}_1=\mathbf r \mid \mathbf q,\mathbf r_0),
\]
for all \(t\). This is doing a lot of work. In the main paper, the assumption is justified only informally by saying that later states provide richer context. That intuition is plausible, but it is not a theorem about the actual decoding distribution, especially when the target \(\mathbf r\) is harmful and the model is safety-aligned. The appendix reportedly checks it empirically, but the main-paper claim still reads stronger than what is established. More importantly, the practical attack objective in **Equation (4)** is only useful insofar as this monotonicity is reasonably stable across prompts and targets, yet the paper does not quantify how often the assumption fails in the main text, nor how attack performance degrades when it is loose. This matters because the non-intervention attack story is one of the paper’s main contributions.

Relatedly, the mathematical exposition around the diffusion likelihood is somewhat underspecified and occasionally sloppy. In **Equation (1)** on **Page 4**, the paper writes the full generation probability using nested integrals over discrete token sequences. Formally this should be expressed as sums over discrete states rather than integrals, unless the authors are intentionally using measure-theoretic shorthand, which is not explained. This is not fatal, but it contributes to a pattern where the probabilistic object is presented somewhat impressionistically. Likewise, **Equation (5)** on **Page 6** presents standard alignment as
\[
\min_{\theta} p_{\pi,m_t}(\mathbf r_T=\mathbf r \mid \mathbf q,\mathbf r_0),
\]
which is more an informal interpretation than the actual training objective used in practice. I think the paper would be stronger if it clearly separated intuitive surrogates from real optimization targets. Right now the method section sometimes slides between them too freely.

The pseudocode and training description have several inconsistencies that make reproduction harder than it should be. In **Algorithm 1** on **Page 7**, line 5 uses \(r^{(i)}_{t_{\min}}\) when the text says the intervention step is \(t_{\mathrm{inter}}\), and line 6 has malformed notation. In **Algorithm 2** on **Page 26**, line 6 computes \(t_{\mathrm{inter}} = \lfloor t_{\min} + \frac{s}{B}(t_{\max}-t_{\min})\rfloor\), which appears inconsistent with the earlier linear schedule definition on **Page 6**, where the denominator is total steps \(S\), not batch size \(B\). This looks like a real typo, not a stylistic issue, because it changes the curriculum schedule. Also, the main paper defines \(\mathcal D_h\) on **Page 6** as harmful query-response pairs, but **Appendix D.4.2** says the full BeaverTails dataset, including harmless pairs, is used. That inconsistency should be resolved in the main paper. Safety papers need especially crisp training definitions.

The empirical story is strong on the tested models, but the architectural breadth is still limited. All three evaluated systems are very similar masked diffusion language models, and one of them, MMaDA, starts from a dramatically different safety baseline. In **Table 1** on **Page 6**, **No Attack** ASR for MMaDA is already \(79.7\%\), which means the model is barely aligned in the first place. Then in **Table 2** on **Page 8**, RA helps a lot on MMaDA, but the interpretation is different from LLaDA and LLaDA 1.5 because the baseline regime is so weak. I do not think this invalidates the results, but it does limit how strongly the paper can claim a general MDLM phenomenon rather than a phenomenon in a narrow family of current masked-denoising implementations.

I also have reservations about the attack evaluation protocol used to instantiate the anchoring attack. In **Section 4.1** on **Pages 4-5**, harmful responses for anchoring are generated by a non-safety-aligned model, and the appendix says these were synthesized and reviewed by humans. That is understandable for constructing a controlled attack, but the main paper does not discuss how sensitive the vulnerability numbers are to the exact style, verbosity, or lexical choice of those harmful targets. Because the mechanism is about specific intermediate tokens serving as anchors, target-response construction could materially affect ASR. For example, shorter harmful responses, more template-like harmful responses, or targets containing continuation cues such as “Sure” or “First” could produce very different attack strengths. The paper would benefit from at least one main-text sensitivity analysis.

The utility evaluation is helpful but still not fully reassuring. **Table 4** on **Page 9** shows average performance staying roughly flat, which is good, but there are nontrivial drops on some tasks, especially HumanEval and PIQA for the LLaDA models. For example, LLaDA HumanEval drops from 22.0 to 17.1, and PIQA drops from 74.4 to 71.6. The paper describes this as no substantial degradation, which feels a bit too casual. I agree the average is mostly preserved, but task-specific regressions deserve a more careful discussion, especially since RA is trained with a safety/usefulness reward model and could plausibly change response style in a way that affects code or reasoning tasks.

A final weakness is exposition quality in a few important places. There are multiple typographical and naming issues in the main paper tables and text, such as “SPT” where the baseline appears to be SFT in **Table 2** on **Page 8**, model names like “ReNeLMA” where the paper earlier discusses MMaDA, and formatting corruption near the baseline description on **Page 7**. These do not destroy the substance, but they do undermine confidence, especially around exact baseline identities and implementation details.

## Questions
1. For **Theorem 4.1** and the surrogate in **Equation (4)**, can the authors report in the main paper, not only the appendix, how frequently the monotonicity assumption fails across prompts and targets, and whether First-Step GCG still outperforms MC-GCG on those failure cases? This would materially increase my confidence in the non-intervention attack contribution.

2. Please clarify the exact optimization target used in RA. In **Equation (7)** on **Page 6**, the objective is written in terms of \(p_{\pi,m_t}\), but **Appendix D.4.1** says gradients are replaced with the first-step mask predictor probability. Is the practical training objective effectively
\[
\max_\theta \mathbb E[\mathcal R(q,r_T)]
\]
with policy-gradient-style credit assignment over sampled trajectories, or is there an additional first-step surrogate used during training? The current description mixes conceptual and implemented objectives.

3. Can the authors fix the pseudocode inconsistencies between **Page 6**, **Algorithm 1** on **Page 7**, and **Algorithm 2** on **Page 26**, especially the use of \(S\) vs. \(B\) in the linear schedule and \(t_{\min}\) vs. \(t_{\mathrm{inter}}\)? A precise correction would help reproducibility.

4. How sensitive are the anchoring results to the choice of harmful target response used for injection? A rebuttal table comparing multiple target constructions, such as short vs. long harmful responses or responses with vs. without explicit affirmative phrases, would substantially strengthen the paper.

5. In **Table 4**, some task-specific drops are noticeable. Can the authors comment on whether these regressions are statistically stable, and whether they stem from style shifts, over-refusal, or reduced helpfulness after RLHF-style alignment?

6. The paper focuses on random remasking schedules used in current implementations. How much of the claimed vulnerability and the effectiveness of RA depend on the property from **Page 4** that once tokens are unmasked they are never re-masked? This seems central to both the monotonicity intuition and the attack mechanism.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper develops and evaluates jailbreak attacks against diffusion language models, including intervention-based attacks and a practical non-intervention attack surrogate. Although the goal is defensive, the work still provides operational attack insights that could lower the barrier to exploiting MDLMs. This concern is directly tied to **Sections 4.1 and 4.2** on **Pages 4-6**, as well as the harmful-response synthesis procedure described later in the paper. I do not view this as disqualifying, but it does warrant ethics-aware handling, careful release choices, and some scrutiny of how attack details are shared.

## Soundness Rating
3: good. The core empirical claims are mostly supported by the experiments, but the theoretical component, especially the reliance on the monotonicity assumption in Theorem 4.1, is not fully nailed down in the main paper, and some methodological descriptions need correction.

## Presentation Rating
3: good. The paper is generally readable and well organized, with effective use of **Figures 1-3** and clear main-message tables, but there are noticeable notation issues, pseudocode inconsistencies, and several typos/table-label problems.

## Contribution Rating
3: good. Identifying a DLM-specific priming vulnerability and proposing a targeted recovery-style alignment method is a meaningful contribution for the MDLM safety literature, even if the current validation is somewhat narrow and the theory is less convincing than the experiments.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a clear and interesting core idea, a defense that is well matched to the failure mode, and solid empirical gains on the tested MDLMs. I am positive overall, but only narrowly, because the main theoretical claim is assumption-heavy, some training/objective descriptions are inconsistent, and the generality beyond the specific masked diffusion setups evaluated here remains somewhat underexplored.

## Reviewer Confidence
4: confident. I am confident in my assessment and checked the main technical and empirical components carefully, though I am somewhat less certain about the exact implementation details because the paper itself is inconsistent in a few places.