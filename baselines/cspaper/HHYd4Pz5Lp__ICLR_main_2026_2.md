---
job_id: 7fa3e788-004d-466e-92f5-c6abab640665
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: HHYd4Pz5Lp.pdf
paper: DelRec: Learning Delays in Recurrent Spiking Neural Networks
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a new training method for recurrent spiking neural networks and evaluates it on machine learning benchmarks for temporal processing.

## Minimum Quality
Pass ✅. The paper includes the core ingredients of a scientific submission, namely abstract, introduction with prior-work positioning, methods, experiments/results, and conclusion; while some exposition and evaluation choices are imperfect, the work is sufficiently complete and technically coherent to merit full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-targeted text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces DelRec, a surrogate-gradient-based method for learning delays in recurrent connections of spiking neural networks. The core idea is to relax integer-valued delays into real-valued ones during training via a triangular interpolation kernel, schedule recurrent inputs into future timesteps with a buffer mechanism, and round delays back to integers at inference. Empirically, the paper reports strong results on SSC, PS-MNIST, and SHD, and argues that learned recurrent delays can be more beneficial than feedforward delays for temporal tasks.

## Strengths
The paper tackles a meaningful and underexplored problem in SNNs, namely how to optimize recurrent transmission delays with a training procedure compatible with surrogate gradients and standard backpropagation. This is a relevant contribution because recurrent delays are biologically motivated and plausibly useful for long-range temporal processing, yet most existing delay-learning work in SNNs has focused more on feedforward connections.

The method itself is intuitive and fairly implementable. The scheduling-buffer view in Section 2.2 and Algorithm 1 gives a concrete operational picture of how future recurrent inputs are constructed, rather than leaving the mechanism as a vague conceptual description. I also appreciated that the paper makes the minimum effective recurrent delay convention explicit, via Eq. 7 and the discussion on Page 4, because this matters for interpreting what a learned parameter \(d=0\) actually means.

Figure 2 is helpful overall. In particular, Figure 2C does a good job illustrating the intended training behavior of the interpolation kernel: broad temporal spreading early in training, then narrowing toward effectively linear interpolation and finally integer rounding. This figure materially improves the reader’s understanding of why the authors anneal \(\sigma\), and it supports the main methodological claim better than the text alone.

The empirical results are potentially strong. Table 1 shows competitive or better performance than a number of prior SNN baselines on SSC and PS-MNIST, and notably the recurrent-delay-only DelRec variant performs best among the DelRec variants on both datasets shown there. If these comparisons are fair, that is a meaningful practical result. I also appreciate that Table 2 is more restrained in its SHD interpretation, and the authors explicitly acknowledge saturation and statistical overlap issues on that benchmark rather than overselling tiny gains.

The functional study in Section 3.2 is a genuine plus. Many papers stop at leaderboard numbers; here, the authors at least attempt to probe when recurrent delays help, under parameter and sparsity constraints. Figure 3C is particularly useful because it suggests a nuanced picture: recurrent delays appear stronger in low-parameter settings, while feedforward delays may have a better accuracy-energy tradeoff at matched firing rates.

The paper is also reasonably reproducible on the surface. The code repository is provided, algorithmic details are given, and several hyperparameter tables appear in the appendix.

## Weaknesses
1. **The claimed methodological novelty is weaker than the paper presents, and the positioning against the most relevant prior work is not sharp enough.**  
   The paper repeatedly emphasizes being “the first SGL-based method to train axonal or synaptic delays in recurrent spiking layers” and “the first method to train axonal or synaptic delays in recurrent connections using surrogate gradient learning” (Abstract, Page 1 to 3). But the same pages already cite a recent recurrent-delay method by Xu et al. using backpropagation and softmax-selected recurrent delays, as well as Mészáros et al. for event-based delay learning. Given that Xu et al. is described by the paper itself as learning a recurrent delay parameter per layer with backpropagation, the real novelty here seems to be a more flexible per-neuron continuous-delay parameterization plus the specific interpolation/scheduling implementation, not the broader concept of recurrent delay learning with gradient-based training. That is still publishable territory, but the framing currently overreaches. This matters because ICLR-level contribution is judged not just by whether results improve, but by whether the conceptual advance over adjacent work is clearly isolated. As written, the paper blurs “first SGL method for recurrent delays” with “first recurrent delay learning idea that works well,” which are not the same claim.

2. **The mathematical exposition has several precision problems, including at least one apparent mistake in the support characterization, and multiple places where the training objective / optimization details are underspecified or inconsistent.**  
   On Page 4, the support statement around Eq. 12 is written as  
   \[
   \forall \tau,\ h_{\sigma,d}(\tau)=0 \Leftrightarrow \tau \in \text{supp}(h_{\sigma,d}),
   \]
   which is backwards. By definition, \(\tau \in \text{supp}(h_{\sigma,d})\) should correspond to nonzero values, not zero values. This is not just cosmetic, because the subsequent argument about only scheduling values over the support is built on this statement. Also, the interval notation for the support is sloppy relative to the strict/non-strict boundary induced by the \(\max(0,\cdot)\) form in Eq. 9.  
   There are more issues. Eq. 10 introduces \(h_{\sigma_{\text{spick}},d_j}\), which looks like a typo or undefined symbol; presumably this should be \(h_{\sigma_{\text{epoch}},d_j}\) or similar. The text says “One can notice in Eq.15” when discussing support immediately after Eq. 11, which suggests equation-number drift and weak proofreading. On Page 3, “We use the surrogate gradient method ()” is missing the citation and looks unfinished.  
   The loss definitions in Eqs. 16 and 18 are also not written correctly in standard cross-entropy notation. Eq. 16 uses \(-\log(\hat y_n, y_n[n])\), which is not a valid scalar expression as written, and Eq. 18 again mixes indices in a confusing way. Since the readout definitions differ across tasks, the exact way logits/probabilities are formed matters for reproducibility. These issues lower confidence that all implementation-critical details are correctly communicated in the main paper.

3. **Algorithm 1 is not fully consistent with the layer-level formulation in the main text, and some indexing choices are ambiguous enough to hinder exact understanding.**  
   The method section distinguishes neurons \(i\) and \(j\), with \(w_{ij}^{\text{rec}}\) denoting the weight from presynaptic \(j\) to postsynaptic \(i\) in Eq. 7. But in Algorithm 1 on Page 13, inside the time loop, the code-like structure first updates \(X_i^{\mathrm{rec}}[t]\), computes \(S[t]\), advances the pointer, then loops over \(j\) and \(\tau\), updating
   \[
   B_j[\cdot] \gets B_j[\cdot] + w_{ji}^{\mathrm{rec}} \cdot \text{spread}[\tau] \cdot S_i[t].
   \]
   This is probably intended to mean “neuron \(i\) emits and contributes to all targets \(j\),” but the symbol conventions are opposite to Eq. 7, and the pseudocode computes \(S[t]\) rather than \(S_i[t]\) in the inner neuron loop a few lines earlier. Those details matter because the main contribution is an algorithm, not just a qualitative idea. Right now the reader has to infer the intended semantics instead of being able to trust the pseudocode as exact. For a method paper, that is a real weakness.

4. **The paper makes strong claims about improving gradient propagation and temporal skip connections, but these claims are not directly validated.**  
   The introduction argues that recurrent delays may mitigate vanishing/exploding gradients by “bridging distant time steps,” and Figure 1B visually illustrates a shorter-path intuition in the computational graph. That is a plausible story, but it remains an intuition in this paper. There is no measurement of gradient norms across time, no comparison of effective credit assignment horizons, no training-stability analysis, and no ablation isolating whether the gains come from better optimization versus extra expressive temporal structure. Figure 1B therefore functions more as a motivational cartoon than evidence. This matters scientifically because one of the paper’s most interesting claims is not simply “delays help,” but “recurrent delays help partly because they improve optimization over long temporal horizons.” Without targeted analysis, that part remains speculative.

5. **The empirical study is good in breadth for a specialized SNN paper, but still narrower than the claims require, especially regarding ablations of the proposed mechanism itself.**  
   The core method has several distinct design decisions: per-neuron axonal delays rather than per-synapse delays in experiments, the triangular kernel \(h_{\sigma,d}\), the annealing of \(\sigma\), the optional learned \(p_i\) modification on SSC (Eq. 15), and integer rounding at inference. Yet the paper does not isolate the effect of these components. For example, there is no ablation comparing fixed \(\sigma\) versus annealed \(\sigma\), no comparison between triangular interpolation and simpler alternatives, no analysis of whether the learned \(p_i\) actually matters on SSC, and no sensitivity study for delay initialization, which appears rather wide in A.2.4. This is important because otherwise it is unclear which ingredients are necessary for the reported gains and which are implementation convenience.

6. **The experimental comparisons in Table 1 are somewhat difficult to interpret fairly, and some supporting evidence is thinner than the headline claim suggests.**  
   Table 1 is central to the acceptance case, but it mixes papers with different neuron models, training protocols, and in at least one case reproduced results versus numbers copied from prior work. The authors do say they deliberately exclude more complex neuron models, which is reasonable, but then the table still includes a heterogeneous set where some methods use recurrence, some feedforward delays, some recurrent delays, some adaptive neurons, and parameter counts are not always precisely known. More importantly, for PS-MNIST the DelRec result is reported on only one seed, justified by saying that previous SOTA papers also use one seed. That may be common practice in this niche, but it is still weak evidence for a SOTA claim, especially when the margin over ASRC-SNN is only \(96.21\%\) versus \(95.77\%\). On SSC, the difference between the best DelRec variant and the previous best listed baseline is also not huge. Table 1 is encouraging, but not yet a knockout empirical case.

7. **Some comparisons that would be most informative are missing from the main paper, especially against simpler recurrent-delay baselines and parameter-matched alternatives.**  
   Section 3.2 includes a useful SHD ablation, but the main large-scale results on SSC and PS-MNIST do not include in-paper ablations against: (i) the same architecture with fixed random recurrent delays, (ii) the same architecture with one learned recurrent delay per layer rather than per neuron, or (iii) a recurrent architecture with a similar increase in parameter count allocated elsewhere. These are important controls because they would help answer whether the gains come from the recurrent-delay learning principle specifically, from merely introducing temporal heterogeneity, or from extra capacity. The SHD study partially touches this, but the paper’s strongest claims are made on SSC and PS-MNIST, where such controls are absent.

8. **The paper’s own results create an underexplained tension about combining recurrent and feedforward delays.**  
   In Table 1, “DelRec (only Rec. delays)” outperforms “DelRec (Rec. and Ff. delays)” on SSC, despite the latter having more parameters. In Table 2 on SHD, the combined model slightly outperforms recurrent-only. In Figure 3C and the accompanying discussion on Page 8 to 9, the combined model does not appear advantageous in small configurations. This is actually interesting, but the paper does not analyze it. Is the issue optimization difficulty when both delay types are learned jointly, overfitting, redundancy, bad hyperparameter transfer from DCLS-style feedforward delays, or simply noise? Without explanation, the paper’s concluding statements about the relative importance of recurrent delays versus feedforward delays feel stronger than the evidence supports.

9. **The computational cost and memory overhead of the proposed method are not characterized in the main paper, despite being an obvious practical concern.**  
   The paper argues that the method is efficient enough for implementation in PyTorch/SpikingJelly, and the circular buffer construction is meant to help. Still, DelRec introduces an additional future-scheduling mechanism whose cost depends on \(\dim(\hat{\mathbf E}(\sigma,D))\), itself tied to the maximal learned delay and \(\sigma\). Eq. 13 suggests the effective buffer length can grow with \(\max_j d_j\), and Algorithm 1 has nested loops over neurons and support positions. Yet there is no empirical timing, GPU memory comparison, or asymptotic discussion against a vanilla RSNN or against feedforward-delay methods. This omission matters because the paper positions DelRec partly as a practical training method, not just a proof of concept. Especially for long sequences such as PS-MNIST, overhead is highly relevant.

10. **Some figures are useful, but others overstate what is actually established by the experiments.**  
    Figure 1A is a nice intuition pump for how a recurrent delay can qualitatively change dynamics from coincidence detection to pattern generation, but it is essentially a didactic toy example rather than evidence about trained models. Figure 1B is even more problematic in that it visually suggests a mitigation of vanishing/exploding gradients, yet no experiment measures this. By contrast, Figure 3 is much more scientifically valuable because it reports actual comparative data. In Figure 3B, the learned recurrent-delay model appears to outperform fixed recurrent delays, vanilla RSNN, and vanilla SNN at roughly matched parameter counts around 10k, which is one of the more convincing pieces of evidence in the paper. I would encourage the authors to lean more heavily on figures like Figure 3 and less on suggestive schematic claims like Figure 1B unless they add targeted validation.

11. **There are several writing and presentation issues that accumulate enough to matter.**  
    Beyond the equation-level problems already noted, the manuscript has many smaller but noticeable issues: inconsistent capitalization of section titles, duplicated punctuation in Figure 2 caption (“matrix..”), odd phrasing such as “strictly superior to 1 spike” in Figure 1 caption, occasional grammar problems, and some citation/year inconsistencies in the references. None alone is fatal, but together they make the presentation feel less polished than expected for a strong ICLR acceptance. This also affects trust in the exactness of the mathematical and experimental descriptions.

12. **The significance claim is somewhat overstated relative to the evidence presented.**  
    The abstract says recurrent delays are “critical” for temporal processing in SNNs. That is stronger than what the paper actually shows. The evidence supports that learned recurrent delays can be beneficial and sometimes outperform feedforward delays, especially in certain low-parameter or long-range dependency settings. But the paper also shows cases where combining delay types is not straightforward, where gains are modest, and where feedforward delays can be more energy-efficient at matched performance. Calling recurrent delays “critical” implies a level of necessity or general dominance that the present experiments do not establish.

## Questions
1. The paper’s central novelty would be much clearer if the authors explicitly contrasted DelRec with the recurrent-delay method of Xu et al. What exactly is the methodological delta, in parameterization, optimization, and practical flexibility? A side-by-side comparison table in the rebuttal would help.

2. Can the authors clarify the mathematics around Eqs. 9 to 13? In particular:  
   - Is the support statement around Eq. 12 a typo, with \(\tau \in \mathrm{supp}(h_{\sigma,d})\) intended to mean \(h_{\sigma,d}(\tau) > 0\)?  
   - What is the correct symbol in Eq. 10, \( \sigma_{\text{spick}} \) vs \( \sigma_{\text{epoch}} \)?  
   - Can the authors provide the exact gradient of \(h_{\sigma,d}(\tau)\) with respect to \(d\), especially at the piecewise boundaries?

3. Algorithm 1 is currently ambiguous in its indexing. Please clarify whether \(w_{ij}^{\text{rec}}\) denotes source \(j \to i\) throughout, and whether the pseudocode line using \(S[t]\) should be \(S_i[t]\). A corrected pseudocode snippet would increase confidence substantially.

4. Could the authors provide a targeted ablation on at least one main dataset comparing: fixed random recurrent delays, one delay per layer, one delay per neuron, and if feasible one delay per synapse? This would help determine whether the gains really come from the specific granularity of learned delays.

5. Can the authors quantify runtime and memory overhead versus a vanilla RSNN and versus feedforward-delay learning? Even rough relative factors on SSC and PS-MNIST would be informative.

6. The results suggest an interesting interaction between recurrent and feedforward delays. Why does recurrent-only beat recurrent+feedforward on SSC in Table 1, while the reverse happens on SHD in Table 2? Is this due to optimization, overfitting, or hyperparameter mismatch? Some explanation or additional evidence could materially change my view.

7. The paper motivates improved gradient propagation via delayed recurrent edges. Do the authors have any direct evidence, such as gradient-norm-over-time statistics, training stability curves, or effective horizon analyses? This would strengthen one of the most interesting claims.

8. For PS-MNIST, can the authors report variance across seeds? Even if prior work uses one seed, a rebuttal with 3 seeds would materially increase confidence in the claimed improvement.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work uses standard public datasets and develops training methodology for spiking neural networks. While the paper mentions neuromorphic hardware deployment, the submission does not raise any specific fairness, privacy, legal, or safety concern that requires dedicated ethics review.

## Soundness Rating
2: fair. The method is plausible and supported by nontrivial experiments, but there are enough issues in mathematical precision, algorithmic specification, and empirical isolation of the key mechanism that I do not think the central claims are supported as cleanly as the paper suggests.

## Presentation Rating
2: fair. The high-level story is understandable and several figures, especially Figure 2 and Figure 3, are useful, but the paper has too many notational inconsistencies, equation/pseudocode issues, and presentation rough edges for a stronger score.

## Contribution Rating
2: fair. Learning recurrent delays in SNNs with surrogate gradients is a relevant direction and the reported results are promising, but the incremental novelty relative to nearby work and the incompletely analyzed empirical story keep the overall contribution below the bar I would expect for ICLR acceptance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
This is a promising paper with interesting ideas and some strong empirical signals, especially the functional study around Figure 3 and the competitive results in Table 1. However, I see too many substantive issues in novelty framing, mathematical exactness, missing ablations on the core mechanism, and lack of computational analysis to recommend acceptance in its current form. With a cleaner positioning and more targeted evidence, this could become a solid conference paper.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with SNN training and delay-learning formulations, and I carefully checked the main technical details and experimental claims, but some implementation specifics would benefit from author clarification.