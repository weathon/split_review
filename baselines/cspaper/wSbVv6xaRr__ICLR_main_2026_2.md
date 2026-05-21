---
job_id: c9bcef7c-071e-42f6-837d-131ec1f233d8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: wSbVv6xaRr.pdf
paper: Communication-Efficient and Private Federated Learning via Projected Directional Derivative
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, focusing on federated learning, communication-efficient optimization, and privacy against gradient inversion attacks.

## Minimum Quality
Pass ✅ The submission includes the expected scientific components, namely abstract, introduction/related work, methodology, experiments/results, and conclusion. While I found important technical and empirical weaknesses, they do not rise to the level of an automatic desk rejection based solely on completeness or obvious procedural violations.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes FedMPDD, a federated learning method that compresses each client’s gradient by sending directional derivatives along multiple random Rademacher directions, plus a seed allowing the server to reconstruct those directions. The paper claims this gives a favorable communication-privacy-accuracy trade-off, with uplink communication reduced from dimension \(d\) to \(m \ll d\), convergence comparable to FedSGD when multiple projections are averaged, and inherent privacy against gradient inversion due to the low-rank projection structure.

The submission provides a convergence analysis for a single-direction variant (FedPDD) and the proposed multi-direction variant (FedMPDD), together with empirical results on MNIST, FashionMNIST, and CIFAR-10 under gradient inversion attacks and communication budgets.

## Strengths
The paper tackles an important combination of problems in federated learning, namely communication reduction and privacy leakage from shared gradients. The core mechanism is simple to describe, reasonably intuitive, and easy to implement at a high level: clients transmit only directional derivative scalars and a seed rather than full gradients.

I also appreciate that the paper does not stop at a one-direction estimator, but explicitly identifies the weakness of the rank-1 version and then proposes the multi-projection extension. That progression, from FedPDD to FedMPDD, gives the paper a coherent narrative and makes the method easier to understand.

The privacy motivation is communicated effectively through the visual evidence. In **Figure 2** on Page 7, the contrast between FedSGD / weak Laplace noise / QSGD and FedMPDD is visually clear: the reconstructions under FedMPDD are much less recognizable than under several baselines, which does support the paper’s practical privacy motivation at least qualitatively. Likewise, **Figure 1** on Page 6, where the SSIM remains low across epochs for FedMPDD, does illustrate the intended claim that the attack success does not obviously spike later in training.

The main experimental tables are also easy to read. For example, **Table 2** on Page 9 does make the central trade-off tangible: under the stated CIFAR-10 budget, FedMPDD stays within a much smaller communication envelope than FedSGD and still achieves nontrivial accuracy, while the reported SSIM is lower than most compression baselines. Even though I have concerns about how to interpret these numbers, the table is at least aligned with the paper’s stated objectives.

Finally, I appreciate that the authors compare against both communication baselines and privacy baselines, instead of evaluating only one axis. Many papers in this area optimize one objective and hand-wave the other; this paper at least tries to place itself at the intersection.

## Weaknesses
I have several substantial concerns, and in my view they affect both the technical soundness and the strength of the claimed contribution.

1. **The central convergence claim is internally inconsistent across the paper.**  
   This is not a cosmetic issue. The **Abstract on Page 1** states that FedMPDD “converges at a rate of \(\mathcal{O}(1/K)\), matching the performance of FedSGD,” while the **Statement of Contribution on Page 2** says the method achieves \(\mathcal{O}(1/\sqrt{K})\), and **Theorem 2 on Page 5** also gives \(\mathcal{O}(1/\sqrt{K})\). Those are materially different rates. A reader should not have to guess which headline theorem is supposed to be true. Since the abstract is the paper’s strongest claim, this inconsistency weakens confidence in the care taken in the analysis.

2. **The use of the Johnson-Lindenstrauss lemma appears mathematically incorrect, and this directly undermines Equation (4) and Theorem 2.**  
   The paper’s main technical step on **Page 5** says that for \(m = O(\ln(d/\delta)/\varepsilon^2)\), the map \(\frac{1}{m}U_{k,i}U_{k,i}^{\top}\) approximately preserves gradient norms, leading to **Equation (4)**:
   \[
   \left\|\frac{1}{m}U_{k,i}(U_{k,i}^{\top}\mathbf g_i)\right\| \le (1+\varepsilon)\|\mathbf g_i\|.
   \]
   In the appendix, **Lemma 6 on Page 29** is stated in an even stronger form: for \(P \in \mathbb R^{m\times d}\) with \(m \ll d\),
   \[
   (1-\varepsilon)\|x\|^2 \le \|Px\|^2 \le (1+\varepsilon)\|x\|^2,\quad \text{for all }x\in\mathbb R^d,
   \]
   and “equivalently” \(\|P^\top P - I_d\|_2 \le \varepsilon\).  
   This “for all \(x \in \mathbb R^d\)” statement cannot hold when \(m<d\), because \(P\) is rank-deficient and has a nontrivial nullspace, so there exist nonzero \(x\) with \(Px=0\). More bluntly, a map from \(\mathbb R^d\) to \(\mathbb R^m\) with \(m<d\) cannot uniformly preserve all norms. Standard JL guarantees apply to a finite set of points, not uniformly to all vectors in \(\mathbb R^d\). Since this lemma is used as the bridge from rank-deficient projections to dimension-independent convergence in **Theorem 2**, the main theorem is not adequately justified as written.

3. **The privacy argument is overstated, and the paper itself contains caveats that substantially weaken the “inherent privacy” narrative.**  
   The main text repeatedly suggests that rank deficiency itself provides a robust defense against gradient inversion, see **Equation (3)** on Page 4 and the discussion on **Pages 5–7**. But the same paper later acknowledges in **Remark 2 on Page 6** and in **Appendix D, Page 25** that privacy is only guaranteed in the worst case as long as \(T\times m < d\). This matters a lot in practice. For the LeNet setup, the paper uses \(m=400,600,800\) in several places, and the training runs are much longer than \(d/m\) rounds for modest-size models. Once enough independent linear measurements are accumulated over rounds, the “underdetermined system” intuition stops being a clean argument.  
   More importantly, the paper conflates “the projected gradient is not uniquely invertible in one round” with “the original private input is protected against GIAs.” Those are not the same statement. Gradient inversion attacks are nonlinear optimization problems over data, not just one-step linear algebra on a fixed gradient. **Lemma 2** tries to bridge this gap, but it relies on assumptions that are not operationally validated in the experiments and still does not establish a strong adversarial privacy guarantee. So the language in the main paper, especially “formal defense against GIAs” on **Page 6**, is too strong for what is actually shown.

4. **Algorithm 2 contains implementation-level inconsistencies that create confusion about the actual method.**  
   On **Page 4**, **Algorithm 2** resets \(\Delta_{\mathrm{sim}}\gets \bar{\mathbf u}_d\) at line 13, but then line 17 updates \(\Delta_{\mathrm{sum}}\), and line 20 aggregates using \(\Delta_{\mathrm{sim}}\). This looks like a bug, not a stylistic typo, because it affects the variable being accumulated and the value used in the final update.  
   There are several other notation issues of the same flavor. On **Page 2**, the projected directional derivative is said to be “defined in (1),” but **Equation (1)** is the global optimization objective, not the projected estimator. On **Page 3**, the notation switches between \(\hat{\mathbf g}\), \(\dot{\mathbf g}\), and projected directional derivative with limited discipline. These issues are not fatal by themselves, but for a paper whose contribution depends heavily on exact estimators and update rules, they do reduce trust.

5. **The theory around reconstruction error and privacy is not as rigorous as the paper presents it.**  
   **Lemma 1 / Equation (6)** on **Page 6** gives the relative gradient reconstruction error as \((d-1)/m\). That quantity actually grows with \(d\), and when \(m\ll d\) it can be enormous. This is not inherently a problem, but the paper repeatedly interprets it as a direct and stable privacy guarantee at the data level. The jump from a projection-induced gradient error to a lower bound on input reconstruction in **Lemma 2 / Equation (7)** depends on a Lipschitz constant \(L_v(\mathbf x)\) of the gradient with respect to the input. This is a strong modeling assumption, and the paper does not explain when it is finite, how large it is for the used networks, or whether the bound is meaningful numerically.  
   Also, the proof in the appendix effectively uses the favorable case \(\mathcal L(\hat v^\star)=0\) to simplify the lower bound, which is not discussed carefully in the main paper. For a security/privacy claim, this is too loose.

6. **The experiments are suggestive, but they do not convincingly validate the strongest claims.**  
   The paper’s main message is joint communication efficiency, privacy, and strong learning performance. However, much of the evidence is built around extremely restrictive byte-budget setups in which some baselines exceed the budget in the first iteration. For instance, in **Table 2** on **Page 9**, FedSGD receives “\(\star\)” under the 0.90 GB budget because it exceeds the budget immediately. This is not surprising and does not teach us much beyond the fact that sending full gradients is expensive. The more interesting comparison would be whether FedMPDD dominates strong compressed baselines at matched total communication or matched accuracy under a broad range of budgets, not just in a regime where dense-gradient methods are eliminated by construction.  
   Similarly, **Table 1** on **Page 8** and **Table 2** on **Page 9** present “defendability” as a binary field, but the paper never really defines a rigorous threshold for that label in the main text. That makes the table look cleaner than the underlying evidence warrants.

7. **The results on \(m\) are not analyzed carefully enough, and some trends are at odds with the paper’s narrative.**  
   The paper argues that increasing \(m\) should improve the estimator and help convergence. Yet in the main tables, larger \(m\) often leads to *worse* final accuracy under fixed budgets, e.g. **Table 1** on **Page 8**, where FedMPDD with \(m=400\) outperforms \(m=600\) and \(m=800\), and **Table 2** on **Page 9**, where \(m=600\) outperforms \(m=2000\). Of course, under a fixed byte budget, larger \(m\) also means fewer rounds, so the trend is not paradoxical. But that is exactly why the current presentation is incomplete. The paper needs a cleaner separation between estimator quality as a function of \(m\), privacy as a function of \(m\), and training progress as a function of total transmitted bits.  
   **Figure 3** on **Page 8** partly addresses this by plotting both communication rounds and transmitted bits, which is useful, but the paper does not analyze the figure with enough precision. As shown there, one can tell different methods cross over depending on whether the x-axis is rounds or bits, and that nuance is central to the paper’s claim. Right now the text leans too hard on a few favorable snapshots.

8. **The computational story is underdeveloped and somewhat self-contradictory.**  
   In **Algorithm 2** on **Page 4**, the client first computes the local stochastic gradient \(\mathbf g_i(\mathbf x_k)\) at line 6 and then computes \(m\) inner products with random vectors. That implies added work on top of standard gradient computation. Yet **Remark 1** on **Page 5** argues that FedMPDD can avoid computing the full gradient and instead use JVPs, but that appears to be a future or alternative implementation rather than the algorithm actually evaluated in the main paper. The remark even states “We empirically evaluate this strategy in our follow-up study (see Section F),” which is not the same as demonstrating it here.  
   Meanwhile, **Table A.10** in the appendix reports tiny latency numbers for computing the directional scalars, but that table does not demonstrate end-to-end client efficiency relative to full gradient training, because line 6 of the actual algorithm still computes the full gradient first. So the paper should not overstate client-side computational advantages.

9. **Several claims are stronger than the evidence given.**  
   On **Page 9**, the paper states that smaller \(m\) values can “actually achieve comparable or even faster convergence” because the projection suppresses some noise and stabilizes optimization. That is an interesting hypothesis, but the paper does not provide a principled analysis for it, and the statement currently reads more like post-hoc storytelling around selected curves. The same applies to some comparisons with LDP on **Pages 5–6** and **Appendix C**. It is fair to say the proposed mechanism behaves differently from additive noise, but the paper often slides from “different” to “better” without sufficiently tight theory or broad empirical validation.

10. **Presentation quality is uneven, despite the high-level idea being understandable.**  
   There are repeated theorem-numbering issues, with **Theorem 2** used both in the main text for convergence and in **Appendix D** for multi-round privacy. There are grammar problems and several places where claims are repeated with slightly different wording rather than sharpened. The core idea is accessible, but the presentation is not polished enough for a paper leaning heavily on formal guarantees.

## Questions
1. The biggest issue for me is the use of JL in **Equation (4)**, **Theorem 2**, and **Appendix Lemma 6**. Can the authors provide a corrected statement and proof? In particular, how do they justify a near-isometry property for \(\frac{1}{m}UU^\top\) when \(U\in\mathbb R^{d\times m}\) with \(m<d\) is necessarily rank-deficient? If the guarantee is only for a fixed vector \(\mathbf g_i(\mathbf x_k)\) or for the sequence of realized gradients rather than uniformly for all \(x\), please state that precisely.

2. Please reconcile the convergence-rate discrepancy between the **Abstract** (\(\mathcal O(1/K)\)) and the rest of the paper (\(\mathcal O(1/\sqrt K)\)). Which claim is intended to be the main one?

3. For privacy, what exactly is the threat model in the multi-round setting? Since the server receives the seeds and can reconstruct all projection vectors, how should one interpret the main-paper claim of “inherent privacy” once \(T m\) becomes comparable to or exceeds \(d\)? A more careful statement about what is and is not protected would significantly increase my confidence.

4. Can the authors provide cleaner experiments that isolate the effect of \(m\)? I would like to see, at minimum, accuracy versus rounds at fixed \(m\), accuracy versus total bits, and privacy versus \(m\), all on the same dataset/model, so the trade-off is not conflated with budget truncation.

5. In **Algorithm 2**, are lines 13, 17, and 20 a typo, or is there some intended distinction between \(\Delta_{\mathrm{sim}}\) and \(\Delta_{\mathrm{sum}}\)? Please correct the pseudocode if this is only a notation mistake.

6. What exactly does the binary “Defendability” column in **Tables 1 and 2** mean? Is there a threshold on SSIM, attack success rate, or visual recognizability? A quantitative definition is needed.

7. If the actual implementation uses the projected-forward/JVP approach discussed in **Remark 1** and **Figure F.1**, please clarify that in the main paper. If not, I would suggest removing or toning down computational-efficiency claims, because the algorithm as written still computes full gradients.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies privacy leakage and defenses in federated learning using standard public datasets and standard gradient inversion attacks. I did not identify an ethics issue that independently requires escalation based on the content provided in the main paper.

## Soundness Rating
1: poor. The main technical claims are weakened by a likely incorrect use of the Johnson-Lindenstrauss lemma, inconsistencies in the convergence statement, and overextended privacy conclusions relative to what is actually proven.

## Presentation Rating
2: fair. The high-level idea is understandable and some figures/tables are helpful, but the paper has important notation inconsistencies, pseudocode errors, theorem-numbering issues, and several places where claims are stronger than the exposition supports.

## Contribution Rating
2: fair. The idea of federated learning through multiple projected directional derivatives is interesting, and the joint communication/privacy framing is relevant, but the current version does not support its strongest claims well enough to count as a solid ICLR contribution.

## Overall Rating
2: Reject, not good enough. The paper has an interesting core idea and some promising empirical signals, but the current submission overclaims on both theory and privacy. In particular, the main convergence argument appears to rest on a flawed near-isometry statement, and the privacy guarantees are substantially less robust than the paper’s framing suggests.

## Reviewer Confidence
4: confident. I am confident in this assessment, especially regarding the mathematical issue around the JL-style argument and the mismatch between the paper’s privacy narrative and its own multi-round caveat.