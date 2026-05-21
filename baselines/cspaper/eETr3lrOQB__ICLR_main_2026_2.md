---
job_id: fdc45315-fa28-4427-ae4b-16bc0fc23cfb
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: eETr3lrOQB.pdf
paper: VQ-Transplant: Efficient VQ-Module Integration for Pre-trained Visual Tokenizers
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in scope for ICLR, focusing on representation learning, generative models, and visual tokenization via vector quantization.

## Minimum Quality
Pass ✅. The submission contains the necessary scientific components, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion; despite some clarity and rigor issues, it clears the bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeted instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes VQ-Transplant, a two-stage framework for replacing the VQ module in a frozen pre-trained visual tokenizer, followed by lightweight decoder adaptation to reduce mismatch between the new quantized latent space and the original decoder. The paper also introduces MMD-VQ, a distribution-aligned quantization variant based on maximum mean discrepancy, and evaluates the approach primarily by transplanting alternative VQ modules into a pre-trained VAR tokenizer across ImageNet-1K and several additional datasets.

## Strengths
The main strength is practical relevance. The paper targets a real bottleneck in modern visual tokenizers, namely that trying a new VQ method usually requires retraining a fairly expensive encoder-decoder-GAN pipeline. Framing this as a “transplant” problem is useful and easy to understand, and the two-stage design in Section 4.1 is operationally simple.

The empirical story is coherent at a high level. In particular, **Table 3** supports the paper’s central claim that simple module substitution alone is not enough, and that decoder adaptation is the key ingredient that recovers or improves reconstruction quality. The contrast between the “Substitution” and “Adaptation” rows is actually one of the most convincing parts of the paper, because it isolates where the gain comes from instead of hiding everything inside one end-to-end recipe.

The paper includes several reasonably informative ablations rather than only headline numbers. For example, **Table 4** and **Figure 3** provide a useful view of how r-FID changes over adaptation epochs, which helps support the claim that a small amount of decoder tuning already gets most of the benefit. Even if the exact choice of 5 epochs is somewhat under-justified, this analysis is still helpful.

The qualitative evidence is aligned with the quantitative narrative. **Figure 2** clearly shows that the substitution stage alone leaves visible blur and detail loss, while decoder adaptation restores sharper structures and textures. This figure is not just decoration, it directly supports the paper’s claim about decoder-quantizer mismatch.

The compute-efficiency angle is potentially valuable to the community. **Table 1** communicates the intended efficiency win clearly, and a framework that lets researchers evaluate new quantizers without paying full tokenizer training cost could be useful even if the individual transplanted VQ variant is not itself a major algorithmic advance.

The presentation of the basic setup is mostly accessible. **Figure 1** gives a clear visual overview of the frozen encoder-decoder, VQ replacement, and adaptation stages. For a systems-style contribution like this, that diagram is doing real work for reader comprehension.

## Weaknesses
1. **The novelty of the core framework is somewhat narrower than the paper suggests, because the method is essentially “replace the quantizer, freeze the rest, then fine-tune the decoder.”**  
   I understand the practical value, but conceptually this is a fairly direct recipe once the decoder-mismatch problem is identified. The paper repeatedly frames this as enabling “plug-and-play integration of arbitrary VQ algorithms” in a broad sense, but the main technical mechanism is modest: Stage I optimizes the new quantizer against frozen encoder features via Equation (3), and Stage II fine-tunes the decoder with standard reconstruction, perceptual, and GAN losses via Equation (4). That is a sensible engineering design, but the paper sometimes sells it as if it were a much deeper methodological decoupling than what is actually demonstrated. This matters for contribution assessment, because the scientific question is not just “does this work,” but also “how much conceptual progress beyond obvious modular fine-tuning does this represent?”

2. **The empirical validation is heavily concentrated on one backbone tokenizer, namely VAR, and the main paper therefore overstates generality.**  
   The abstract and introduction repeatedly suggest arbitrary or broadly applicable pre-trained visual tokenizers, yet the core evidence in the main paper is almost entirely VAR-based. The only non-VAR evidence appears in Appendix D for LDM-16, and even there the results are notably weaker. Since the review must be based on the main paper, the broad claim of tokenizer-agnostic transplantability is not really established. This matters because the central premise is framework generality, not just “a good trick for VAR.” The paper should either narrow its claims or provide stronger main-paper evidence across materially different pretrained tokenizers.

3. **Several comparisons in the main benchmark table are not fully fair or are at least difficult to interpret, because token counts, codebook sizes, architectures, and training regimes differ substantially.**  
   In **Table 2**, MMD VQ and MMD VAR are compared against a broad mix of prior tokenizers, but many of these baselines use different token budgets, codebook sizes, and likely different architectures or training pipelines. The paper highlights that MMD VQ with 512 tokens and MMD VAR with 680 tokens achieve excellent r-FID, but this is not an apples-to-apples benchmark against 256-token baselines. The issue is not that the authors should magically equalize all prior work, but that the paper draws fairly strong ranking claims from a table where the settings are heterogeneous. Since reconstruction quality in tokenizers is strongly affected by token count and codebook size, this weakens the force of the “outperform competing baselines” claim in Section 5.

4. **The compute-efficiency comparison in Table 1 is useful but methodologically thin, and the headline speedup claims are more fragile than presented.**  
   **Table 1** compares VQ-Transplant trained on ImageNet-1k for 22 hours on 2 A100s against several tokenizers trained on ImageNet-1k or OpenImages with very different settings. This is directionally informative, but it is not a controlled cost comparison. Some rows use OpenImages, some use ImageNet-1k, the base architectures are not aligned, and the table excludes the cost of pretraining the tokenizer that VQ-Transplant relies on. Of course the framework intentionally amortizes that cost, so ignoring it is not inherently wrong, but then the claim should be phrased more carefully as incremental adaptation cost rather than overall tokenizer development cost. Right now the paper blurs those two notions in a way that makes the 21.8x or 95% savings sound stronger than the evidence strictly supports.

5. **The mathematical exposition around the objective is underspecified in several places, and this matters because the paper’s main mechanism is optimization-based.**  
   Start with **Equation (3)**. The loss is written as
   \[
   \mathcal{L}_{\text{VQ}}(\phi)=\|\operatorname{sg}(z_e)-z_q(\phi)\|_2^2+\gamma \mathcal{L}_{\text{unique}}(\mathcal{Q}^{\text{new}}_\phi).
   \]
   But this omits several details needed to reproduce or understand the optimization dynamics. Over what set is the norm aggregated, individual spatial locations, batch averages, or both? Is there no commitment-style term analogous to the second stop-gradient term in standard VQ-VAE objectives, and if not, why is this stable across all transplanted variants? For fixed-scale transplantation, the paper says 32-D features are split into two 16-D subvectors and quantized independently, but the exact objective over those split branches is not formalized. If the method is supposed to be generic across VQ variants, the paper should be more explicit about what is shared and what remains algorithm-specific.

6. **The MMD-VQ contribution is only weakly differentiated from prior distribution-matching VQ methods, and the main paper does not do enough to justify why MMD is the right design beyond a generic “non-Gaussianity” argument.**  
   Section 4.2 argues that MMD is preferable to Wasserstein VQ because it does not assume Gaussianity. However, in the main-paper experiments the empirical gains over Wasserstein VQ are quite small and inconsistent. For example, in **Table 3** at 8192 codebook size after adaptation, MMD VAR improves r-FID from 0.83 to 0.81 over Wasserstein VAR, which is positive but modest. In **Tables 8 and 10**, Wasserstein VQ is sometimes better than MMD VQ after adaptation. So the main paper’s own evidence suggests MMD-VQ is a competitive alternative, not clearly a stronger quantizer in general. The stronger argument about non-Gaussian synthetic data is relegated to Appendix B, which cannot bear the main burden of contribution. This matters because the paper claims two contributions, but the second one is not convincingly established in the main text.

7. **The paper frequently interprets lower quantization error as evidence of better compatibility or less information loss, but the causal story is not rigorously established.**  
   In Section 5.1, the authors argue that distribution-alignment methods are more compatible because they achieve lower quantization error and better downstream reconstruction after adaptation. But quantization error here is computed with respect to frozen encoder features, which may or may not correspond to the latent statistics the pretrained decoder expects. Indeed, the paper itself shows that lower quantization error before adaptation does not necessarily mean better reconstruction than the original VAR tokenizer. So “lower \( \mathcal{E} \)” is at best a partial diagnostic, not a sufficient notion of compatibility. The discussion in Section 5 sometimes slips from correlation into stronger claims than the evidence warrants.

8. **Some tables contain notation inconsistencies or unclear column naming that hurt trust in the presentation.**  
   For example, **Table 5** uses columns labeled \(I(\downarrow)\) and \(D(\uparrow)\), while analogous quantities elsewhere are denoted \( \mathcal{E} \) and \(U\). **Table 6** uses \(l(\downarrow)\) and \(l4(\uparrow)\), which look like formatting or transcription mistakes rather than intentional notation. These are not fatal on their own, but they are exactly the kind of sloppiness that makes it harder to verify what is being measured and compared. Since the paper asks readers to trust fairly fine-grained quantitative differences, notation hygiene matters.

9. **The cross-dataset generalization section is interesting but scientifically weaker than it appears because the baselines are sparse and the setup favors the transplanted model.**  
   In Section 5.3, **Tables 8 to 10** present strong reconstruction results on FFHQ, CelebA-HQ, and Churches. However, the comparisons are uneven: Table 8 includes literature baselines for FFHQ, but Tables 9 and 10 mostly compare only Wasserstein VQ and MMD VQ under the proposed framework. More importantly, these experiments reuse a pretrained tokenizer and adapt it to new datasets, while the cited baselines may be fully trained under different settings. Without a carefully matched adaptation-vs-full-training protocol, the “state-of-the-art” style framing is too strong. This matters because generalization claims are one of the headline selling points in the later part of the paper.

10. **The qualitative figures support the paper’s narrative, but they also reveal that the claimed gains are mostly about preserving reconstruction quality within a very favorable setting, not about broader robustness.**  
    **Figure 2** is effective, but it is based only on MMD VAR. It would have been more informative to include side-by-side qualitative results for at least one weaker transplanted quantizer, such as EMA or vanilla VQ, to show whether the adaptation mechanism itself is robust or whether success is mostly due to choosing a good replacement quantizer. Likewise, **Figures 4, 5, and 6** show visually plausible reconstructions on FFHQ, CelebA-HQ, and Churches, but there is no failure-case analysis, no zoomed detail comparison, and no evidence about semantic consistency under more difficult domains. The figures support the best-case story, but not the limits of the method.

11. **The “from-scratch vs transplant” comparison is not especially persuasive as presented.**  
    In **Table 6**, the from-scratch models are trained for only 5 to 7 epochs, and then the paper concludes that they perform much worse than VQ-Transplant. That conclusion is unsurprising and, frankly, a bit too easy. The text even acknowledges that high-quality discrete tokenizers typically need hundreds of epochs from scratch. If so, this table mainly confirms that undertraining is bad. A more meaningful comparison would normalize by equal wall-clock budget, or compare against stronger partial-training baselines such as decoder warm-starting, or limited joint fine-tuning from the pretrained tokenizer without explicit “transplant” staging. As it stands, Table 6 strengthens the efficiency narrative less than the authors seem to think.

12. **There are a few mathematical and notational issues that should be corrected for precision.**  
    In **Equation (8)** in the appendix, the Wasserstein distance expression appears to be missing an equals sign before the square root term. More importantly for the main paper, Section 4.2 states that MMD with characteristic kernels guarantees universal distribution matching, but the practical estimator in **Equation (5)** is the empirical squared MMD over finite samples \(X\) and codebook vectors \(Y\). The paper should be more careful in separating the population statement \( \mathcal{D}_{\text{MMD}}^2(P,Q)=0 \iff P=Q \) from the finite-sample optimization actually performed. This is not a fatal theorem error, but the current wording is a bit too loose for a paper leaning on theory-flavored motivation.

## Questions
1. The paper claims VQ-Transplant can integrate “arbitrary” or broadly applicable VQ modules into pre-trained tokenizers. Can the authors substantially narrow or clarify this claim? In particular, based on the main paper, what are the actual conditions required of a VQ module for Stage I and Stage II to work reliably?

2. Please clarify the exact optimization used in **Equation (3)**. Over what tensor dimensions is the squared error aggregated, how is it normalized, and why is there no explicit commitment loss term of the form \( \| z_e - \operatorname{sg}(z_q)\|_2^2 \) in Stage I? A precise formulation would increase confidence that the method is reproducible and stable.

3. Can the authors provide a stronger justification for the compute claims in **Table 1**? Specifically, are these intended to represent incremental cost for evaluating a new quantizer on top of an already trained tokenizer, or total cost of obtaining the final tokenizer system? The current framing mixes those interpretations.

4. The paper’s strongest evidence is VAR-based. Do the authors have main-paper-level evidence, not appendix-only evidence, that the framework works comparably on a materially different pretrained tokenizer family? Even a compact additional experiment or a more explicit limitation statement would help.

5. In **Table 2**, many baselines differ in token count and codebook size. Can the authors temper the “outperform competing baselines” claim, or provide a more controlled comparison to baselines with matched token budgets? This would make the benchmark interpretation cleaner.

6. The improvement of MMD-VQ over Wasserstein VQ is modest in the main paper and sometimes reversed on other datasets. What concrete evidence would the authors point to, within the main paper, that MMD-VQ is more than just another reasonable distribution-matching variant? If the answer relies primarily on non-Gaussian synthetic evidence from the appendix, the paper should say so more explicitly.

7. **Figure 2** is persuasive for MMD VAR. Could the authors add or discuss analogous qualitative evidence for weaker transplanted quantizers, such as vanilla or EMA-based variants, to help disentangle the importance of the framework from the importance of the specific replacement quantizer?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work studies image tokenization and reconstruction on standard public datasets and does not present an obvious fairness, privacy, or safety issue beyond those already typical for generative vision models.

## Soundness Rating
3: good. The central empirical claims are mostly supported, especially the utility of decoder adaptation after VQ replacement, but several comparisons are not as controlled as the paper’s language suggests, and parts of the mathematical/objective specification are underspecified.

## Presentation Rating
3: good. The paper is generally readable and the high-level framework is clearly illustrated, especially in Figure 1, but there are enough notation inconsistencies, overstatements, and underspecified equations to prevent a higher score.

## Contribution Rating
3: good. The framework is practically useful and likely valuable for researchers working on visual tokenizers under limited compute, but the conceptual novelty is moderate and the MMD-VQ contribution is not fully convincing as a distinct main-paper advance.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has clear practical value, a coherent empirical story around modular VQ replacement plus decoder adaptation, and enough evidence to make the framework interesting for the community. At the same time, the claims are broader than the evidence, the evaluation is too concentrated on VAR, and the MMD-VQ component is only modestly supported as a separate contribution.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main empirical and mathematical claims carefully, though some implementation-specific details are still underspecified in the paper.