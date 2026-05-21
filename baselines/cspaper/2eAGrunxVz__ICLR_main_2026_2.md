---
job_id: d77e7d88-3096-4cc0-8e60-965a9756ef66
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2eAGrunxVz.pdf
paper: Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies diffusion generative models, latent-space watermarking, statistical distribution preservation, and provenance for ML-generated images.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, theoretical analysis, experiments, ablations, discussion, and conclusion; despite some overstatements and clarity issues, it meets the minimum bar for a full technical review rather than a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Spherical Watermark, a lossless, encryption-free watermarking method for diffusion models that embeds user-specific bits into the initial Gaussian latent without modifying model weights. The core pipeline combines a binary mixing matrix with random padding, a mapping from binary codes to points on the sphere, an orthogonal rotation, and chi-square scaling to recover Gaussian-like noise. Experiments on Stable Diffusion show strong image fidelity, near-chance detectability by classifiers, faster embedding/extraction than prior lossless methods, and improved tracing robustness under several attacks.

## Strengths
The paper tackles a timely and practically relevant problem. Provenance for diffusion outputs matters, and the focus on lossless watermarking without per-image key storage is meaningful. Relative to prior latent watermarking schemes, the proposed design is conceptually clean: binary repetition plus randomized mixing, then spherical mapping and rotation.

The empirical section is broad and generally convincing on the main practical axes the paper cares about, namely undetectability, extraction accuracy, and runtime. In particular, **Table 1 (Page 7)** is a strong piece of evidence that the method does not noticeably degrade output distribution as measured by FID; the numbers for "Ours" are essentially on top of "Original" across both datasets and both backbones, and are also competitive with or slightly better than PRC Watermark. This is important because the paper’s central pitch is that watermarking should preserve the latent prior rather than visibly perturb generation quality.

The detectability experiments are useful and more informative than reporting image quality metrics alone. **Figure 2 (Page 7)** shows that Tree-Ring and fixed-key Gaussian Shading are separable both at the latent and image level, while PRC and the proposed method remain near chance. This directly supports the paper’s claim that preserving the prior matters for hiding the watermark signal from learned detectors. I also appreciated that the figure includes both training loss and test accuracy, which helps rule out trivial undertraining explanations.

The runtime comparison is another concrete strength. **Figure 4 (Page 8)** makes the computational story visually obvious: extraction for PRC is dramatically slower, while the proposed method is lightweight. Since the paper explicitly positions itself against cryptographic-code-heavy alternatives, this figure supports an actual systems-level advantage rather than a purely mathematical one.

The robustness results are strong overall. **Table 2 (Page 8)** shows that the proposed method is highly competitive with Gaussian Shading on clean and adversarial settings and substantially better than PRC under post-processing. The gains are not just cosmetic, they matter for real provenance systems where routine transformations are common. Likewise, **Figure 5 (Page 9)** gives a more granular picture across attack types and shows that the method’s advantage over PRC is fairly consistent.

The ablation studies are reasonably targeted. **Figure 6(b,c) (Page 9)** helps isolate the roles of the binary embedding and spherical mapping modules, and **Table 3 (Page 10)** provides a useful robustness trade-off over \(s\) and \(N\). Even though I have some concerns about how some of the theoretical claims are framed, the experimental ablations do suggest that the individual modules are not arbitrary engineering choices.

Finally, the paper is ambitious in trying to connect a practical watermarking system with a structured statistical argument. Even if I do not fully buy all of the wording of the theoretical claims, the attempt to reason through the distributional properties of the latent code is better than the usual purely empirical story.

## Weaknesses
1. **The strongest theoretical claim is overstated relative to what is actually established in the main paper.**  
   The abstract and introduction repeatedly suggest that the final watermarked noise is distributed like exact standard Gaussian noise, or is "statistically indistinguishable" from it, while the actual main-paper theory in **Section 3.3 (Pages 5 to 6)** only establishes much weaker facts: 3-wise independence of \(\mathbf{z}^{(1)}\), a spherical 3-design property for \(\mathbf{z}^{(2)}\), invariance of this property under orthogonal rotation for \(\mathbf{z}^{(3)}\), and an asymptotic marginal Gaussian statement in **Lemma 3.3**. This is not the same as proving \(\mathbf{z}_w \sim \mathcal{N}(\mathbf{0}, I)\) jointly. In fact, **Theorem 3.2** and **Lemma 3.3** only imply matching of low-order moments and asymptotic one-dimensional marginals, not full multivariate equivalence. The paper itself partly admits this in **Section 5 (Page 10)** by saying the guarantee depends on spherical 3-designs and higher-order moments may deviate. That admission undercuts the stronger wording elsewhere. This matters because the main security and undetectability narrative is phrased as if a much stronger distributional guarantee had been proved.

2. **There is a gap between the formal security definition and the actual evidence provided.**  
   In **Equation (2) and Equation (3) (Page 3)**, the paper defines undetectability using computational indistinguishability against any probabilistic polynomial-time adversary, with negligible advantage in a security parameter \(\rho\). But the subsequent theory does not operate in a computational cryptography framework, and the experiments in **Figure 2** only test relatively simple detectors, namely a two-layer MLP and ResNet-18. There is no reduction from the proposed construction to a standard hardness assumption, and there is no argument that 3-wise independence plus spherical mapping implies negligible distinguishing advantage for arbitrary efficient adversaries. As written, the formal security definition is far stronger than what the paper supports. The paper would be much more sound if it reframed this as statistical approximation or empirical undetectability under tested detectors, rather than cryptographic indistinguishability in the sense of **Equation (2)**.

3. **The extraction pipeline relies on assumptions that are stronger than the paper acknowledges, especially around inversion and conditioning mismatch.**  
   The method description in **Equation (11) and Equation (12) (Page 5)** uses conditional generation for embedding but empty-condition inversion for extraction. The paper states that this simulates real-world settings, but it does not really analyze why the watermark should remain recoverable under such a mismatch, beyond empirical redundancy from repetition coding. Since extraction accuracy hinges on recovering the correct sign pattern after reversing diffusion and VAE encoding, the conditioning mismatch is not a minor implementation detail, it is central to the method’s reliability. **Table 4** and **Table 5 (Page 10)** show limited sensitivity to solver/timestep choices, which is reassuring, but they do not fully explain why the inverse ODE under \(\varnothing\) should be faithful enough when the forward sampling used text conditioning. The method evidently works empirically, but the exposition treats this as more straightforward than it is.

4. **Some mathematical statements and notation are sloppy or internally inconsistent, which hurts trust in the theoretical section.**  
   A few examples:
   - In **Section 3.3 (Page 5)**, the text says it will prove the final code \(\mathbf{z}_w\) is distributed as \(\mathcal{N}(\mathbf{0}, I_{l_x})\), but the theorem chain only supports a weaker approximation.  
   - In **Theorem 3.2 (Page 6)**, the theorem alternates between discussing a random vector and "the finite set of \(\mathbf{z}^{(2)}\)", which are not the same object unless the support is made explicit.  
   - In **Equation (10) (Page 5)**, the radius is sampled independently via \(r^2 \sim \chi^2(l_x)\), but the later exact-Gaussian argument in **Lemma 3.4** requires a uniform direction on the sphere, not merely a spherical 3-design or asymptotically Gaussian marginals.  
   - In the appendix proof of **Lemma 3.3**, the normal approximation argument relies on a dependency-graph Stein bound and then treats the maximum degree \(D\) as effectively constant because \(N\) and \(l_m\) are "preset constants". But in the actual system \(l_m\) is not a fixed mathematical constant in any asymptotic sense, it is a tunable parameter and can be large. So the asymptotic statement is somewhat slippery.  
   These are fixable, but they matter because the theory is a major selling point of the paper.

5. **The evaluation of undetectability is narrower than the paper’s claims.**  
   The paper uses FID, an MLP latent classifier, and a ResNet-18 image classifier. That is a decent start, but the claim language is broader than the evidence. For example, **Figure 2 (Page 7)** only reports one dataset/model setting for image-level classification, and the main paper relies on the appendix for broader classification plots. In addition, FID in **Table 1** is computed against the unwatermarked output distribution, but FID is a coarse metric for subtle prior shifts. If the paper wants to emphasize "statistically indistinguishable," stronger two-sample tests, likelihood-ratio proxies, or larger-capacity detectors would better match that claim. As is, the evidence supports "hard to detect with our tested classifiers," not "indistinguishable" in the formal sense used earlier.

6. **The baseline comparison is strong on the selected set, but the paper’s positioning against other Gaussian-prior-based tracing approaches still feels a bit narrow.**  
   The paper compares mainly against Tree-Ring, Gaussian Shading, and PRC on the latent side, plus several classical image watermarking baselines. That is reasonable, but given how central the "lossless Gaussian-prior watermarking without key overhead" angle is, the paper would benefit from more careful positioning against the broader family of recent latent Gaussian modulation or communication-style tracing approaches. Even without adding full experiments, a sharper discussion of where the present method sits relative to other Gaussian-prior-preserving designs would help the originality claim land more cleanly. Right now, the paper is convincing that it improves over the specific baselines in **Table 2** and **Figure 5**, but somewhat less convincing that it has fully mapped out the nearby design space.

7. **The practical trade-offs on capacity, robustness, and redundancy are not fully unpacked in the main paper.**  
   The method’s effective message capacity depends on the repeated structure \(l_x = N l_m + l_r\), and robustness depends strongly on \(N\) and \(s\). **Figure 6(a) (Page 9)** and **Table 3 (Page 10)** are useful, but the main paper does not explicitly discuss the effective rate in bits per latent dimension, nor how one should choose \(N\), \(l_r\), and \(s\) under a target threat model. This matters because one of the paper’s practical arguments against PRC is better trade-off management, yet the actual operating frontier is only partially characterized. For a deployment-oriented provenance method, a more explicit rate-robustness-undetectability analysis would increase scientific value.

8. **The qualitative presentation is somewhat selective and does not fully stress-test failure modes.**  
   **Figure 3 (Page 7)** shows example images across methods and, visually, the proposed outputs look clean. However, the figure mostly functions as a reassurance figure rather than as an analysis tool. It would be more informative if the paper included examples where inversion or extraction fails, or where different methods behave differently under specific attacks. Similarly, **Figure 5 (Page 9)** presents ACC/TPR trends under multiple attacks, but the strongest discrepancies would be easier to interpret if the paper linked them to actual reconstructed latents or bit-error patterns. The paper is strong on headline metrics, weaker on explaining the residual failure modes.

9. **Some presentation details are rough for a paper that leans heavily on theory.**  
   The exposition is generally readable, but several passages require extra effort. For example, the relation between \(\mathbf{T}\), \(\mathbf{R}\), the index set \(P\), and the 3-wise independence claim in **Algorithm 1 and Equation (6) (Page 4)** is not as transparent as it should be. Likewise, the use of \(\mathcal{G}\) both as the diffusion generator in **Section 3.1** and as the "Diffusion Integration Module" in **Section 3.2** is mildly confusing. None of this is fatal, but it does make the paper harder to parse than necessary.

## Questions
1. The main-paper wording often suggests that \(\mathbf{z}_w\) is Gaussian, while **Section 5 (Page 10)** acknowledges only a spherical 3-design style guarantee with possible higher-order deviations. Can the authors precisely restate the strongest theorem they believe is actually proved in the main paper? In particular, do they claim exact equality in distribution, asymptotic marginal normality, or only matching moments up to degree 3 plus empirical indistinguishability?

2. For the formal security notion in **Equation (2)**, what is the intended interpretation of the security parameter \(\rho\)? If the authors do not have a computational reduction, would they be willing to weaken the claim to an empirical or low-order statistical notion of undetectability? A clear answer here would increase my confidence substantially.

3. In **Equation (11)** generation uses conditioning, while **Equation (12)** extraction uses empty conditioning. Why is this mismatch expected to preserve the watermark reliably? Is the success mainly due to redundancy from repetition and majority vote, or is there a deeper invariance argument? A more explicit discussion would help.

4. Could the authors provide a cleaner statement of the achievable rate-robustness trade-off under the constraint \(l_x = N l_m + l_r\)? For instance, for a fixed latent dimension, how should one choose \(N\) and \(l_r\) to hit a desired target TPR under JPEG or brightness attacks? **Table 3** is useful, but a more systematic operating-curve view would make the method easier to compare to alternatives.

5. The undetectability experiments in **Figure 2** are encouraging, but did the authors test stronger latent-space detectors, for example deeper MLPs, transformers, or two-sample tests on raw latent distributions? I am not asking for an appendix dump, but a concise statement of how robust the "near chance" result is to detector capacity would help calibrate the security claim.

6. In **Figure 6(b,c)**, removing either module hurts performance, but the causal story is still a bit compressed. Could the authors clarify whether the gain from spherical mapping comes primarily from equal-energy signaling after rotation, from better robustness to inversion noise, or from both? This matters for understanding whether the design is principled or just a favorable engineering point.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper is about watermarking and provenance for generated images, which is generally aligned with responsible use of generative models. I do not see a concrete ethics issue in the submission that would require separate escalation based on the material presented in the main paper.

## Soundness Rating
3: good. The method is well motivated and empirically supported, but the strongest theoretical and security claims are overstated relative to what is actually shown in the main paper.

## Presentation Rating
3: good. The paper is mostly readable and reasonably structured, though the notation and theory exposition could be tightened, and several claims need more careful phrasing.

## Contribution Rating
3: good. The paper makes a meaningful contribution on lossless latent watermarking for diffusion models, especially in combining strong empirical performance with a simple encryption-free design, even if the theoretical positioning is somewhat overclaimed.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about the paper’s theoretical wording, especially the jump from low-order moment matching to stronger Gaussian and security language. Still, the practical method is strong, the empirical evidence is broad, **Table 1**, **Table 2**, **Figure 2**, **Figure 4**, and **Figure 5** support the main claims well, and the design offers a useful improvement over prior lossless watermarking baselines. I would recommend acceptance, with the expectation that the authors significantly tone down and sharpen the theory and security claims in the camera-ready version.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main technical concerns, though some appendix-level proof details would still benefit from author clarification.