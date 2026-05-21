---
job_id: facdc24a-adb4-4550-ac3c-6f8f2accb7d9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 3icvqeC1sA.pdf
paper: ChaosNexus: A Foundation Model for Universal Chaotic System Forecasting with Multi-Scale Representations
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning and foundation-model-style transfer for chaotic dynamical system forecasting, with applications to physical sciences and time series ML.

## Minimum Quality
Pass ✅. The submission contains all core scientific sections, presents a complete method and substantial experiments, and while I have significant concerns about novelty, experimental framing, mathematical specification, and presentation quality, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes ChaosNexus, a pretrained forecasting model for chaotic systems built around a U-Net-like hierarchical Transformer called ScaleFormer, augmented with per-block Mixture-of-Experts routing and a wavelet-scattering-based frequency fingerprint. The model is trained on a large synthetic corpus of chaotic ODE systems using a combination of pointwise MSE, MoE load balancing, and an MMD regularizer aimed at preserving long-term attractor statistics. Experiments cover zero-shot forecasting on a large synthetic benchmark, few-shot transfer to weather forecasting, and scaling analyses with respect to model size and training-data composition.

## Strengths
The problem is important and well motivated. Forecasting chaotic systems under data scarcity, while preserving long-term attractor properties rather than only short-horizon pointwise accuracy, is a meaningful target for the ICLR community. I also appreciate that the paper does not evaluate only with standard forecasting error, but includes attractor-oriented metrics such as correlation-dimension error, KL divergence between attractors, Lyapunov-exponent error, and spectral-energy error. That is a good methodological instinct for this domain.

The architecture is reasonably coherent. The central design, namely a hierarchical encoder-decoder Transformer with patch merging/expansion for multiscale temporal processing, is well aligned with the paper’s stated hypothesis that chaotic dynamics contain information across multiple temporal scales. Figure 1 is helpful here: the top-level overview, together with the patch merging / expansion diagrams and the Transformer block with MoE routing, makes the intended information flow much easier to understand than the text alone. In particular, Figure 1(b) clarifies the temporal-resolution changes induced by patch merging / expansion, and Figure 1(c) clarifies where sparse expert specialization sits relative to attention and residual connections.

The synthetic benchmark is large in scale. Evaluating on thousands of held-out chaotic systems is stronger than the typical “three canonical systems and done” standard that unfortunately still appears in parts of the literature. The scaling study in Figure 4 is also useful, especially because it separates parameter scaling from two different notions of data scaling. Even if I am not convinced all claims around these plots are new, it is still valuable to document these trends.

There is some evidence that the multiscale design matters. The ablation table in Appendix Table 1, although not in the main paper, suggests that removing patch merging/expansion or MMD hurts attractor fidelity noticeably. Among those ablations, the degradation from removing patch merging/expansion is one of the cleaner pieces of support for the paper’s central design thesis.

The weather transfer experiment is interesting as an application-level stress test. Figure 3 shows a large gap between ChaosNexus and the system-specific baselines included there, especially at long horizons, and the fact that the zero-shot curve is competitive before any weather fine-tuning is at least intriguing.

## Weaknesses
1. **The paper’s novelty relative to the most directly competing chaotic foundation-model line is not sharply established.**  
   The main text repeatedly positions ChaosNexus against Panda and DynaMix, but much of the overall framing, dataset choice, evaluation setup, and several headline claims look quite close to the existing chaotic-foundation-model paradigm rather than a clearly differentiated contribution. On Pages 1 to 2, the paper emphasizes pretraining on many synthetic chaotic systems for zero-shot and few-shot adaptation, then trains on the Panda corpus itself (Page 2), evaluates on the same style of held-out synthetic systems (Page 7), reports similar attractor-oriented metrics, and reaches a very similar scaling takeaway about system diversity mattering. The claimed conceptual advance is essentially “explicit multiscale architecture + MoE + frequency fingerprint,” which is plausible as an incremental architectural improvement, but the manuscript is written as if it introduces a much broader new principle. Right now the paper undersells how much is inherited from prior work and oversells how far the present step moves the field. This matters because ICLR standards are not just about getting a somewhat better model on an existing benchmark; the paper needs a cleaner delineation of what is genuinely new in problem formulation, methodology, and empirical insight.

2. **The strongest empirical claims are overstated relative to the evidence shown in the main paper.**  
   The abstract and introduction use fairly strong language about “state-of-the-art” and “notable improvements,” but Figure 2 on Page 7 paints a more mixed picture. ChaosNexus is only competitive, not clearly dominant, in short-horizon sMAPE, and even for the long-term metrics the boxplots still show substantial overlap with Panda. The inset mean plots help, but they do not erase the fact that the distributions overlap materially. I am not saying the gains are nonexistent, but the framing is much stronger than the evidence supports. If the main contribution is better long-term statistical fidelity, the paper should report effect sizes and practical significance more soberly rather than jumping from modest aggregate improvements to broad claims about learning “intrinsic dynamics” instead of “superficial pattern memorizing.” That leap is too rhetorical for the evidence presented.

3. **The weather experiment is intriguing but not yet persuasive as a clean demonstration of cross-system generalization.**  
   In Section 4.2, ChaosNexus is pretrained on a synthetic chaotic ODE corpus and then evaluated on WEATHER-5K, while the system-specific baselines are trained from scratch on tiny subsets. That setup certainly demonstrates data efficiency, but it confounds architecture, pretraining, and domain alignment. A stronger test would isolate whether the gain comes from the multiscale architecture specifically, from having seen a large pretraining corpus at all, or from the chaotic-domain pretraining distribution. The paper references Panda and Chronos-S-SFT in the appendix, but the main paper’s Figure 3 only shows system-specific baselines plus ChaosNexus. Since the text on Page 8 makes strong claims about zero-shot weather performance and the advantage of chaotic pretraining, it is a real omission not to show the closest pretrained chaotic baselines alongside the main headline figure. This matters because otherwise the reader is left comparing a pretrained model to mostly non-pretrained models and being asked to accept a fairly sweeping conclusion.

4. **Several experimental comparisons are not especially fair or complete.**  
   On Page 7, the paper evaluates a mixed bag of baselines, but only Chronos receives an explicit domain adaptation variant in the main comparison. If the goal is to test whether general-purpose foundation models can adapt to chaotic data, it is odd that Chronos gets a special fine-tuned version while the other large pretrained models do not appear with analogous adaptation. Conversely, if the goal is to test true zero-shot transfer, then the inclusion of Chronos-S-SFT alongside purely zero-shot models muddies the story. Table 2 in the appendix also has signs of inconsistency and naming drift, for example the metric names differ from those in the main text, “Parrot” appears as “Purtot,” and some metric labels are duplicated or renamed in ways that make the comparison harder to trust at face value. These may sound like presentation issues, but they undermine confidence in careful baseline handling.

5. **The mathematical specification of the model and losses is too loose in places, and some equations are not internally clean.**  
   There are several points that need tightening:
   - In Section 3.1, the number of patches is defined as \(S=\lfloor T/D \rfloor + 1\) for “non-overlapped temporal patches.” For non-overlapping patches, this expression is strange unless there is padding, but padding is not stated. If \(T\) is divisible by \(D\), this gives one extra patch. Since later tensor shapes depend on \(S\), this is not a harmless typo.
   - Equation (2) on Page 5 says the MoE output is the shared expert plus a sum over all \(M\) specialist experts, with \(\phi_{i,p}=0\) outside TopK. That is okay in principle, but the notation mixes sparse and dense formulations without specifying whether gradients flow through the hard TopK operator, whether routing is token-wise or patch-wise over both temporal and variable dimensions, and how the shared expert interacts with normalization of the specialist weights. As written, \(\phi_{M+1,p}\) is a sigmoid gate while \(s_{:,p}\) is a softmax over experts, so the shared expert is not on the same probabilistic scale as the sparse specialists. This can be a valid design, but it is mathematically underspecified and not discussed.
   - Equation (7) on Page 6 defines the final forecast using \(\text{Concat}(\mathbf{H}_{\text{uni}}, \mathbf{F}_w)\), but the text immediately before introduces the temporally pooled fingerprint as \(\bar{\mathbf{F}}_w\), not \(\mathbf{F}_w\). The notation is inconsistent exactly at the point where the conditioning variable enters the predictor.
   - Equation (10) is described as using “batches of the full predicted and ground-truth trajectories,” but the notation \(\kappa(\hat{\mathbf{X}}^i,\hat{\mathbf{X}}^j)\) leaves unclear whether the kernel is applied to flattened trajectory vectors, state marginals, or some other representation. Since MMD is central to the long-term-statistics claim, this is too important to leave vague.

   These issues matter because the paper’s technical contribution is not merely empirical; it asks readers to trust a specific architectural and objective design, and right now parts of that design are only semi-specified.

6. **The MMD section contains a correctness issue in how the estimator is described.**  
   On Page 29 to 30, Equations (15) to (17) present population MMD, and the text then says “This expression leads directly to the unbiased empirical estimator used in our work as the regularization loss \(\mathcal{L}_{\text{reg}}\).” However, Equation (10) in the main paper uses the standard biased \(V\)-statistic style estimator with all \(i,j\) pairs divided by \(B^2\), including diagonal terms. An unbiased \(U\)-statistic estimator would exclude self-similarity terms and use \(B(B-1)\) denominators for the within-sample sums. This is not a fatal flaw, but it is a concrete mathematical inconsistency between the claim and the equation. The paper should either state clearly that it uses the biased estimator, or revise Equation (10) if unbiasedness is intended.

7. **The exposition is rougher than it should be for a paper with this many moving parts.**  
   There are repeated grammar issues and several artifacts that look like unfinished drafting. Examples include “can generalizes” in the abstract, “encoder blocks progressively builds” on Page 5, and several appendix placeholders such as “ADD” and “REVISE” on Pages 16 to 27. Some of this appears in supplementary material, but it still signals lack of polish. More importantly, there are content-level clarity problems: the paper alternates between \(D_{\mathrm{step}}\), \(D_{\mathrm{avg}}\), \(D_{exp}\), \(D_{\mathrm{stop}}\), \(D_{mn}\), and other inconsistent metric names across the main paper and tables. Table 2 is especially messy in this respect, even duplicating \(D_{exp}\). When a paper uses a battery of nonstandard metrics, naming consistency is not optional. Right now readers have to reverse-engineer whether a metric in the appendix is the same as one in the main text.

8. **Some ablation evidence cuts against the paper’s narrative, and the manuscript does not confront that honestly.**  
   Appendix Table 1 is awkward for the “frequency fingerprint” story. Removing the frequency fingerprint appears to improve, not worsen, both sMAPE@128 and sMAPE@512, while only slightly worsening some long-term metrics. Yet Section A.1 says “Removing the wavelet transform-based frequency fingerprint results in a noticeable decrease in model performance.” That is simply not what the displayed numbers show for pointwise metrics. This is exactly the kind of thing that makes reviewers grumpy, because the table is right there. If the authors believe the fingerprint helps selectively on attractor fidelity or transfer, then say that specifically. Do not claim broad improvement when the ablation is mixed and partially unfavorable.

9. **The figure-based interpretability claims are interesting but too speculative for the certainty with which they are written.**  
   Figure 5 on Pages 9 to 10 visualizes patch partitions and attention maps, and the text then infers that shallow encoder layers act like Toeplitz-like filters, deep decoder layers “function primarily as a selector,” and shallow decoder layers “anticipate future dynamics.” These are vivid interpretations, but they are still interpretations of attention maps, not controlled evidence of mechanism. The plots are visually suggestive, especially the contrast between more localized and more global attention, and I do think Figure 5 supports the broad claim that different layers attend differently across scales. But the more detailed causal story goes well beyond what the figure can prove. This matters because the paper leans on these analyses to justify architectural intuition; they should be presented as hypotheses supported by visualization, not as established facts.

10. **The paper claims a scaling “guiding principle” that is not convincingly isolated from benchmark-specific reuse.**  
   Figure 4(b,c) on Page 9 is useful, but the conclusion that “generalization stems from the diversity of training systems, rather than sheer data volume” is too absolute. First, the plots show relative insensitivity in one setting and stronger gains in another, not a universal law. Second, the distinction between “time points” and “systems” may be entangled with the way the synthetic corpus is generated and augmented. Third, the paper itself cites prior work that already pointed in this direction. So even if the empirical trend is real here, the rhetorical packaging as a guiding principle for scientific foundation models feels larger than what is actually established.

11. **The evaluation of computational trade-offs is too underdeveloped for a model that adds substantial architectural complexity.**  
   The paper adds hierarchical encoder-decoder processing, MoE routing, and wavelet scattering. Yet the efficiency analysis is tucked into Appendix Table 3 and not integrated into the main discussion. Table 3 shows ChaosNexus taking \(0.119\)s versus Panda’s \(0.048\)s for the same 512-step forecast, which is a nontrivial slowdown, roughly 2.5x. That may well be worthwhile, but the paper should discuss this in the main text if it wants readers to adopt the architecture as a practical foundation model recipe. “Better metrics, more compute” is a reasonable tradeoff; pretending the compute question barely exists is not.

12. **The “foundation model” framing is somewhat inflated relative to the actual setup.**  
   I do not object to domain-specific foundation-model language in principle, but the paper stretches the term rather aggressively. The model is trained on a synthetic chaotic ODE corpus with around \(0.35\)B time points according to Table 9, and the base variant has roughly 21M activated parameters / 58M total parameters according to Table 10. This is not inherently a problem, but it means the paper should be more careful in equating its setting with the broader expectations around foundation models. What is demonstrated here is closer to a pretrained domain model for chaotic forecasting than a broadly universal dynamical foundation model.

## Questions
1. The main synthetic comparison in Figure 2 suggests gains over Panda mainly on long-term attractor-style metrics, with only competitive pointwise accuracy. Could the authors quantify the practical significance of these gains more carefully, for example by reporting paired effect sizes in addition to significance markers, and by breaking down how often ChaosNexus wins per system rather than only showing aggregate boxplots?

2. Please clarify the patching formula in Section 3.1. For non-overlapping patches, why is \(S=\lfloor T/D \rfloor + 1\)? Is there implicit padding, or is this an error? Since all later tensor shapes depend on \(S\), this should be unambiguous.

3. For Equations (2) to (4), how exactly is routing performed? Is expert selection applied per temporal patch, per variable-token, or per flattened token over both axes? Are the TopK scores renormalized after truncation? How does the separately sigmoid-gated shared expert interact with the specialist mixture numerically?

4. For Equation (10), what objects are fed into the kernel \(\kappa\)? Are trajectories flattened into a single vector in \(\mathbb{R}^{HV}\), are states pooled across time, or is the kernel computed over some learned feature representation? Also, the paper describes the estimator as unbiased, but Equation (10) appears to be the biased \(V\)-statistic form. Please clarify.

5. Figure 3 is one of the headline experimental results, yet the most relevant pretrained chaotic baselines are not included in the main figure. Could the authors provide the same weather comparison including Panda and Chronos-S-SFT directly in the main-text framing, not only in the appendix, so the reader can separate the value of chaotic pretraining from the value of the proposed architecture?

6. The frequency fingerprint ablation in Table 1 looks mixed and even favorable to removing the fingerprint on sMAPE, which seems inconsistent with the text’s conclusion. Can the authors reconcile this? In what regimes does the fingerprint actually help, and is the benefit mainly on attractor metrics, weather transfer, or something else?

7. The interpretability discussion around Figure 5 is more certain than the evidence warrants. Can the authors tone this down or supplement it with a more quantitative analysis, for example correlation between attention concentration and forecast horizon, or controlled comparisons across systems with known dominant timescales?

8. The scaling conclusion from Figure 4 is stated very broadly. Could the authors rephrase it more carefully as an empirical trend on this benchmark unless they can provide stronger evidence that it is not an artifact of the corpus construction and augmentation scheme?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper. The work uses synthetic chaotic systems and publicly available weather data, and the manuscript does not raise immediate issues involving privacy, human subjects, or sensitive deployment claims.

## Soundness Rating
2: fair. The paper contains a plausible method and substantial experiments, but several key claims are overstated, some comparisons are not fully clean, and important parts of the mathematical specification are inconsistent or underspecified.

## Presentation Rating
2: fair. The high-level story is understandable and some figures are helpful, especially Figure 1 and Figure 2, but notation drift, inconsistent metric names, drafting artifacts, and equation-level ambiguities significantly hurt clarity.

## Contribution Rating
2: fair. There is a meaningful engineering combination here and the empirical direction is relevant, but the contribution feels incremental relative to closely related prior work, and the manuscript does not delineate that sufficiently well.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles an important problem and has some promising empirical evidence, especially on long-term chaotic statistics, but the combination of incremental novelty, overstated claims, incomplete main-text comparisons, and nontrivial clarity / mathematical-specification issues leaves it short of the bar for me in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with the relevant modeling setting and checked the main equations, figures, and tables carefully, but some implementation specifics remain unclear from the paper.