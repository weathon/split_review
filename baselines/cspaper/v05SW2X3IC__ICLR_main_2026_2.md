---
job_id: 8df8c18b-e970-44fd-a1bd-3a25edc48cf7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: v05SW2X3IC.pdf
paper: Lossy Common Information in a Learnable Gray-Wyner Network
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining representation learning, learnable compression, multitask vision, and information-theoretic analysis of learned representations.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion, and it presents a coherent technical contribution with nontrivial theory and empirical evaluation.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes a learnable three-channel Gray-Wyner-inspired codec for pairs of vision tasks, with one common channel and two task-specific private channels. The paper develops a training objective intended to navigate the transmit-receive tradeoff from lossy common information theory, presents a specific neural architecture to encourage common/private separation, and evaluates the approach on a synthetic setup, colored MNIST, and two real computer vision task pairs from Cityscapes and COCO.

## Strengths
The paper has a clear motivating problem. The setting of efficient distributed inference across multiple dependent tasks is meaningful, and the Gray-Wyner lens is a sensible way to formalize the tension between joint transmission efficiency and per-task retrieval efficiency.

The paper does more than just paste an information-theoretic name onto a standard multitask autoencoder. The formulation around transmit rate \(R_t\), receive rate \(R_r\), and the role of the common-channel cost parameter \(\beta\) is conceptually coherent, and the intended operational meaning is easy to follow.

I appreciated the effort to connect the learning objective back to classical quantities. In particular, the discussion around Equations (9) to (12) on Pages 5-6 gives a reasonably interpretable bridge from the Gray-Wyner objective to a practical neural training loss with entropy models. Even if some assumptions are strong, the overall mapping from theory to implementation is better articulated than in many papers that invoke information theory only rhetorically.

The synthetic experiment is actually useful rather than decorative. Figure 3 on Pages 8-9 is one of the more convincing parts of the paper, because it directly visualizes the claimed effect of \(\beta\) on the common-channel rate and the transmit/receive tradeoff. In particular, Figure 3a supports the core claim that training with \(\beta=1\) pushes more information into the common channel, while larger \(\beta\) reduces common usage. Figure 3b-3d also give a concrete architectural comparison, not just a single headline number.

The architecture is also presented clearly at a high level. Figure 2 on Page 6 helps the reader understand how the common representation \(Y_0\) conditions the entropy models for the private channels, and why the decoder for each task uses the concatenation of \(Y_0\) with its private code. This figure does real explanatory work rather than serving as filler.

The empirical results are reasonably broad for the paper’s scope. The paper includes a synthetic setup with partial controllability, an edge-case classification benchmark with known common-information structure, and real vision tasks on Cityscapes and COCO. That combination gives a better picture of behavior than a single benchmark would.

There are some genuinely encouraging quantitative outcomes. For example, Tables 7 and 8 in the appendix show that the proposed method often improves transmit rate relative to the Independent baseline while staying closer to the Joint baseline in task performance. On Cityscapes, Table 7 shows the proposed method consistently lowering \(R_t\) versus Independent at comparable task metrics, and on COCO, Table 8 shows a similar pattern. These numbers do support the paper’s core practical claim that introducing a common channel can reduce redundancy across tasks.

## Weaknesses
1. **The theoretical contribution is interesting, but the main paper does not provide enough detail to assess its correctness and scope confidently.**  
   Theorem 1 on Page 4 is central to the paper’s conceptual positioning, but the proof is deferred entirely to the appendix, and the statement in the main paper is terse enough that several important points remain hard to parse. For instance, Equation (6) and Equation (7) use \(\tilde{\mathcal Z}^{(r)}_{D_1,D_2}\) in both inequalities in the main text, whereas the appendix theorem uses \(\hat{\mathcal Z}^{(t)}_{D_1,D_2}\) in the middle term. If this is a typo in the main paper, it is not minor, because it changes the meaning of the bound. A theorem that is used to motivate the entire optimization story should not force the reader to guess whether the main-text statement is correct. This matters because the claimed separation between lossy Wyner and Gács-Körner quantities is one of the paper’s main conceptual contributions.

2. **The derivation of Theorem 2 relies on very strong existence assumptions that weaken its practical significance.**  
   On Page 5, Theorem 2 assumes that there exist \(f_0,f_1,f_2,g_1,g_2\) in the chosen function families that achieve \(T(\alpha_1,\alpha_2;D_1,D_2)\). This assumption is doing a lot of work. In practice, the architecture is heavily constrained, deterministic, quantized, and optimized only approximately. Under this assumption, the theorem essentially rewrites information quantities as entropies of deterministic codes. That is mathematically understandable, but much less informative as a statement about the actual learned system. Put differently, the theorem is valid only after assuming away the hardest representational issue, namely whether the chosen parametric family can realize the optimum of the Gray-Wyner objective. The paper should be more explicit that this is a representability reduction, not a characterization of the practical neural optimization problem.

3. **Equation (14), which defines the common representation, is quite ad hoc and raises differentiability and optimization questions that are not resolved in the main paper.**  
   On Page 7, the common channel is formed by exact elementwise equality of \(Y_0^{(1)}\) and \(Y_0^{(2)}\), with zeros otherwise:
   \[
   [Y_0]_i =
   \begin{cases}
   \frac{1}{2}([Y_0^{(1)}]_i+[Y_0^{(2)}]_i), & [Y_0^{(1)}]_i=[Y_0^{(2)}]_i\\
   0, & \text{otherwise.}
   \end{cases}
   \]
   This is a brittle mechanism. Exact matching after quantization is a very strong condition, and the paper acknowledges that the auxiliary loss in Equation (15) can either make the common channel unused or collapse the distribution. That is already a warning sign that the mechanism is unstable. More importantly, the paper does not explain what gradient signal flows through the equality test itself, beyond the informal statement that averaging “ensures that gradients flow to both inputs wherever elements match.” The problem is precisely what happens when they do not match. Since common-information formation is the core architectural novelty, the optimization behavior of this masking rule should be analyzed much more carefully.

4. **The architecture/method mismatch with the earlier information-theoretic setup is not fully reconciled.**  
   In Section 2.1 the paper starts from a setting with sources \(X_1\) and \(X_2\) and explicitly assumes the Markov conditions in Equation (1). But in Section 3.3 on Page 7, the authors state that each branch has access to both sources and that this “effectively removes the requirement for the conditions in 1.” Then in Section 4, the experiments specialize to a single source \(X\) with \((X_1,X_2)=X\). This sequence makes the problem formulation slippery. Is the theory about two correlated sources, or about two tasks on one source, or about a codec that takes duplicated access to the same source in two branches? These are related but not identical setups. The paper should do a cleaner job separating the general Gray-Wyner source-coding formulation from the actual multitask single-image implementation. As written, the reader is asked to accept a somewhat loose transfer from one regime to another.

5. **The empirical baseline set is decent but still incomplete relative to the paper’s claims about isolating common information.**  
   The comparisons are mainly against Joint, Independent, and the authors’ own Separated/Combined ablations. That is useful, but it leaves a gap with respect to prior representation-learning methods that explicitly try to decompose shared and private factors. Section 2 cites VAE-style disentanglement work and Dubois et al. (2021), but the experiments do not include any learned shared/private-latent baselines adapted to the task-pair setting. If the paper’s message is that the Gray-Wyner perspective gives a better way to isolate common information than more intuitive or generic disentangling strategies, some empirical contact with that broader family would strengthen the case substantially.

6. **The real-data experiments show utility, but they do not convincingly demonstrate that the learned common channel corresponds to “common information” in a substantive sense rather than merely a helpful side-information bottleneck.**  
   On Page 10, Figure 5 shows that the method often sits between the Joint and Independent baselines, which is directionally sensible. However, the paper’s stronger interpretive claims go beyond “this helps compression” and toward “this distills common information between tasks.” For Cityscapes and COCO, there is no analysis of what is actually encoded in \(Y_0\), how much task-relevant overlap it captures, or whether the common channel is semantically shared rather than just statistically convenient for the entropy model. Figure 5 is therefore supportive of the rate-accuracy tradeoff claim, but not of the stronger representational claim. A method can beat Independent coding without truly disentangling common from private information in the advocated sense.

7. **Some of the strongest claims are supported mainly by appendix content, not by the main paper itself.**  
   The main paper says the performance difference between architectures is theoretically justified by a compatibility analysis, but this justification appears only in Appendix C. Likewise, the actual proof details for Theorems 1 and 2 are outside the main text. Per the main-paper-only standard, this weakens the contribution because an ICLR reader should not need the appendix to understand the validity of the headline claims. The main text currently reads a bit like “trust us, the theory is in the back.” That is not ideal when the theory is part of the stated novelty.

8. **There are several clarity and notation issues that get in the way of careful reading.**  
   A few examples: on Page 3, the distortion definitions are written as \(D_1 = d_1(\tilde Z_1,Z_1)=\mathbb E[d_1(\tilde Z_1,Z_1)]\) and \(D_2 = d_2(\tilde Z_2,Z_2)=\mathbb E[\tilde d_2(\tilde Z_2,Z_2)]\), which mixes function values and expectations, and switches notation from \(d_2\) to \(\tilde d_2\). On Page 4, the sentence “For the conditions in 3 to hold, \(U\) must have at least the mutual information between \(\hat Z_1\) and \(\hat Z_2\)” is too informal and not really a precise mathematical statement. There are also a few typographical inconsistencies, such as the malformed \(\beta\) entries in Table 4. None of these alone is fatal, but together they make the theory harder to trust than it should be.

9. **The use of frozen downstream task models complicates the interpretation of the compression results.**  
   In Section 4.3 and Appendix D.5, the synthesis transform is attached to frozen pretrained task networks, and the paper notes on Page 27 that this effectively encourages input reconstruction, producing relatively large rates. The additional reconstruction loss is admitted to help despite sounding somewhat counterintuitive. This means the empirical system is not purely optimizing task sufficiency; it is partly optimizing compatibility with fixed front ends of pretrained models. That is a pragmatic choice, but it blurs the paper’s claim that the learned channels reflect task information requirements. Some of the bitrate may simply be paying for the representational preferences of those frozen models.

10. **The result presentation is promising but sometimes oversold.**  
   The conclusion on Page 10 emphasizes an average BD-rate advantage of \(-81.58\%\) in transmit rate against single-task codecs. That headline sounds strong, but the method is also explicitly not matching the receive-rate efficiency of Independent coding in the real-task experiments, and the curves in Figure 5 are still noticeably above the Joint baseline. I am not objecting to reporting the gain, but the framing should better reflect that this is a tradeoff result, not a uniformly dominant codec. The paper is strongest when it presents itself as a practical exploration of the Gray-Wyner tradeoff, and weaker when it edges toward sounding like a generally superior multitask codec.

11. **The table evidence is supportive but also reveals unresolved behavior that deserves discussion.**  
   Tables 3, 4, and 5 on Pages 23-24 show that the Shared architecture often improves \(R_t\) and \(R_r\) over Separated, but the Combined architecture occasionally attains even lower \(R_t\) at high \(\eta\), for example Table 4 at \(\eta=1.0\) and Table 5 at \(\eta=1.0\). That does not invalidate the overall message, but it weakens any blanket claim that Shared is consistently best. The paper mentions rate-distortion curves and BD-rates, but a more explicit discussion of where Shared loses and why would make the empirical story more honest and more useful.

## Questions
1. In the main-text statement of Theorem 1 on Page 4, is the middle inequality intended to be
\[
\max_{(\hat Z_1,\hat Z_2)\in \tilde{\mathcal Z}^{(r)}_{D_1,D_2}} I(X_1,X_2;\hat Z_1;\hat Z_2)
\le
\min_{(\hat Z_1,\hat Z_2)\in \tilde{\mathcal Z}^{(t)}_{D_1,D_2}} I(X_1,X_2;\hat Z_1;\hat Z_2),
\]
rather than using the receive-optimal set on both sides? Please clarify whether this is a typo or whether I am misunderstanding the notation. This point matters a lot for confidence in the theoretical contribution.

2. Can the authors explain more concretely how gradients behave through Equation (14)? In particular, what happens when \([Y_0^{(1)}]_i \neq [Y_0^{(2)}]_i\), and how often do matches occur during training at different rate regimes? A rebuttal with statistics on the matching rate, channel utilization, and sensitivity to \(\gamma\) would increase my confidence in the architectural design.

3. How sensitive are the main conclusions to the exact common-channel construction? For example, what happens if the authors replace the hard equality rule in Equation (14) with a soft similarity gate or a learned merging function? If the same tradeoff behavior persists, that would suggest the contribution is robust and not dependent on a brittle implementation detail.

4. For the real-task experiments, can the authors provide evidence that \(Y_0\) actually carries shared task information rather than merely side information that improves entropy coding or compatibility with frozen backbones? Any qualitative probing, decoder-from-\(Y_0\)-only experiment, or mutual-predictability analysis on Cityscapes/COCO would help.

5. Please comment on the role of the frozen downstream models. If those models were jointly finetuned with the codec, would you expect the rates to decrease substantially? Right now the paper itself notes that the frozen models likely force partial image reconstruction. Clarifying whether this is a limitation of the current implementation versus a deliberate part of the formulation would help the reader interpret the bitrate numbers.

6. In Figure 5, the proposed method is close to Joint in some regimes and much better than Independent in transmit rate, which is good, but the receive-rate curves remain above Independent. Did the authors try \(\beta \neq 1\) on the real datasets as well? Since the whole paper is about navigating the transmit-receive tradeoff, it would be useful to know whether the same control observed in Figure 3 appears on Cityscapes and COCO.

7. Table 4 and Table 5 suggest that the Combined architecture can sometimes have lower \(R_t\) than Shared at high \(\eta\). Can the authors explain those cases? Are they noise, or is there a meaningful regime where stronger coupling is preferable to the proposed shared/common split?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper as written. The work studies compression and representation learning for standard vision benchmarks and does not present an obvious fairness, privacy, safety, or human-subjects issue in the main paper.

## Soundness Rating
3: good. The overall technical story is plausible and empirically supported, but several theoretical statements and the main common-channel construction would benefit from clearer justification and tighter presentation.

## Presentation Rating
3: good. The paper is generally readable and the figures are helpful, but there are enough notation issues, theorem-statement ambiguities, and main-text dependence on the appendix that I cannot rate the presentation higher.

## Contribution Rating
3: good. The paper offers a worthwhile bridge between Gray-Wyner theory and learnable multitask codecs, with meaningful experiments and an interesting formulation, though the empirical validation of “common information” itself is still somewhat indirect.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real idea, a coherent motivation, and useful experiments, and I do think it is worth discussion at ICLR. At the same time, the theory-to-method bridge is looser than the paper sometimes suggests, and the evidence for genuine common/private disentanglement is not yet as strong as the rate-distortion plots imply.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main technical concerns, though some of the information-theoretic details would benefit from author clarification.