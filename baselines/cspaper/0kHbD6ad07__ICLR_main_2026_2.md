---
job_id: f12140e3-8bec-436f-86b1-93c5899bc5f8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0kHbD6ad07.pdf
paper: Language Models Are Injective and Hence Invertible
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, combining representation learning, learning theory, interpretability, and privacy/safety implications for language models.

## Minimum Quality
Pass ✅. The submission contains the expected scientific structure, presents a clear theoretical claim with formal statements and proofs, and includes empirical evaluation and algorithmic validation; while I have concerns about scope, positioning, and some proof-to-practice gaps, these are not desk-reject-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-targeted text, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies decoder-only Transformers as functions from discrete prompts to hidden representations, and argues that, under real-analyticity assumptions and standard continuous initialization/training, the map from prompts in $\mathcal{V}^{\le K}$ to the last-token hidden state is almost surely injective. It further claims that this property is preserved after any finite number of gradient descent steps, and proposes SIPIT, a sequential inversion procedure that reconstructs the exact input prompt from per-position hidden states at a fixed layer with a worst-case linear bound in $T|\mathcal{V}|$.

Empirically, the paper reports large-scale collision searches across several pretrained LMs, including GPT-2, Gemma, Llama, Mistral, and Phi variants, finding no observed collisions under numerical thresholds. It also evaluates SIPIT on prompt reconstruction tasks and reports exact recovery with substantial speedups over a brute-force ablation and a prompt-optimization baseline.

## Strengths
1. The paper tackles a surprisingly fundamental question, whether standard decoder-only LMs are information-preserving with respect to discrete prompts, and formulates it in a mathematically crisp way. That reframing, from “components are non-injective” to “the overall discrete-to-continuous prompt map is almost surely injective,” is genuinely interesting and relevant for representation learning, interpretability, and privacy.

2. The main theoretical narrative is coherent and ambitious. The progression from Theorem 2.1, establishing real-analyticity, to Theorem 2.2, showing pairwise collision sets are measure zero, and then to Theorem 2.3, arguing preservation under training, is logically well organized in the main paper. I also appreciated that the paper is explicit about the object of study, namely the last-token representation $\mathbf r(\mathrm s;\theta)$ in Equation (29), rather than vaguely talking about “representations” in general.

3. The witness-style argument in Section 2 is a real strength. In particular, the proof sketch around Equations (2)-(4) does not merely invoke a generic measure-zero slogan, it tries to show concretely why $h(\theta)=\|\mathbf r(\mathrm s;\theta)-\mathbf r(\mathrm s';\theta)\|_2^2$ is not identically zero by constructing parameter settings that separate prompts differing either at the last token or at an earlier position. Even if some details are deferred, that is the right proof strategy.

4. The paper does more than prove a structural property, it operationalizes it. The SIPIT construction in Section 3 is conceptually simple and leverages causality nicely: once the prefix is known, the next token is identified by the position-$t$ hidden state. Theorem 3.1 and Theorem 3.2 state correctness and robustness in a form that is easy to understand.

5. The empirical section is broad in model coverage. Table 1 and Table 3 are useful because they show the minimum pairwise $\ell_2$ distances across very different families and scales, rather than limiting the paper to a single toy GPT-2 result. The fact that these minima remain positive at early, middle, and final layers supports the claim that collision-freedom is not an artifact of one architecture or one depth.

6. A figure-specific strength: **Figure 3** is one of the more persuasive visual elements in the paper. The left panel summarizes per-layer minimum distances for GPT-2 and Gemma families, and the right panel zooms into GPT-2 Small across depth. The important point is not just “nonzero values exist,” but that the distances appear comfortably above the chosen collision threshold throughout, and often increase with depth. That visually reinforces the claim that separability is not marginal or numerically fragile in these tested models.

7. Another useful empirical component is **Figure 5**, which examines distance as a function of sequence length. The observation that the minimum distance rises quickly and then stabilizes is helpful because it addresses a natural concern that longer contexts might induce representational crowding. This does not prove anything exhaustive, but it is a sensible diagnostic.

8. The comparison in **Table 5** is also valuable. Even though HARDPROMPTS is not a perfect task match, the table clearly shows that the proposed sequential exploitation of causal structure is far more efficient than either a generic prompt optimization baseline or a brute-force enumeration baseline. That helps justify SIPIT as more than a restatement of injectivity.

## Weaknesses
1. The title and several headline claims are stronger than what the main theorem actually establishes. The paper title says “LANGUAGE MODELS ARE INJECTIVE AND HENCE INVERTIBLE,” while the main result on Pages 2-4 is explicitly an **almost-sure** statement under a fairly specific assumption set: finite vocabulary, finite context length, decoder-only architecture, real-analytic components, at least one attention head per block, and finite-horizon GD with step sizes in $(0,1)$. This distinction matters. “Injective almost surely over parameter draws, for a restricted architecture class, at finite horizon” is not the same as “language models are injective” in the unconditional sense. The wording on Page 2, “collisions in practical settings form a measure-zero set, and neither initialization nor training will ever place a model inside that set,” is rhetorically punchy, but mathematically it is still a statement about absolutely continuous parameter laws, not a universal theorem over all implementations and all training pipelines.

2. The step from measure-theoretic genericity to practical invertibility is somewhat overstated. Theorems 2.2 and 2.3 are about exact equality, that is, whether $\mathbf r(\mathrm s;\theta)=\mathbf r(\mathrm s';\theta)$ ever happens. But in practice, what matters for privacy leakage and for algorithmic inversion is often **near-collision geometry**, not exact equality. The experiments use floating-point thresholds and pairwise $\ell_2$ distances, but the central theoretical story does not characterize how small $\Delta_{\pi,t}$ may become as a function of depth, width, layer, or prompt family. This matters because exact injectivity with exponentially tiny margins can still be computationally or numerically useless. Theorem 3.2 introduces $\Delta_{\pi,t}$ and a robustness condition $\|\mathbf e_t\|_2<\Delta_{\pi_t,t}/2$, but the paper does not provide a nontrivial lower bound or even a systematic empirical distribution of these margins over prefixes. So “injective” and “efficiently invertible in practice” are not as tightly connected as the framing suggests.

3. The training-preservation argument in Theorem 2.3 is the part I found least convincing from the main paper alone. The sketch on Page 4 relies on the claim that a GD step $\phi(\theta)=\theta-\eta \nabla \mathcal L(\theta)$ is real-analytic, that $\det D\phi$ is real-analytic and not identically zero, and hence that the pushforward of an absolutely continuous law remains absolutely continuous. That argument is plausible, but there are two issues. First, the paper states this for “gradient descent with step sizes in $(0,1)$,” which reads oddly specific, since the relevant condition should be about avoiding singular Jacobians, not the interval $(0,1)$ per se. Second, the proof sketch says “one can check this by evaluating at a simple parameter setting,” which is doing a lot of work. In the appendix, this witness depends on a specially chosen zero-gated unembedding construction. That may be correct, but in the main paper the preservation claim is presented with a level of generality that outpaces the clarity of the justification.

4. There is a technical clarity issue in **Theorem 2.1 / Equation (1)**. The theorem says the map
\[
(\mathrm s,\theta)\mapsto \mathbf r(\mathrm s;\theta)
\]
is “real-analytic jointly in the parameters and the input embeddings.” But $\mathrm s$ itself is discrete, so the theorem as written mixes a discrete object and an analytic notion over Euclidean variables. The later appendix makes clear that, for each fixed sequence $\mathrm s$, the map in the continuous parameters is analytic, and that embeddings are treated as continuous selected rows. But the main-paper wording is imprecise. This is not a cosmetic nitpick, because the whole measure-zero logic depends on analyticity in the continuous variables only. I would strongly recommend rewriting Theorem 2.1 to avoid any suggestion that the prompt index itself participates in a joint analytic map.

5. The empirical collision search is supportive, but limited relative to the claims. On Pages 7-8 the paper reports around 5 billion pairwise comparisons over 100k prompts and no collisions. That sounds large, but the actual prompt space $\mathcal V^{\le K}$ is astronomical, and the sample is drawn from a mixture of four corpora. So these experiments can only show absence of collisions on a sparse slice of the space, not “confirm” injectivity in any strong statistical sense. The paper does acknowledge this in the exhaustive test discussion, but the overall narrative still leans too heavily on the scale of the comparison count. The number of pairwise checks is much less important than the coverage of the structured prompt space where hard near-collisions might live.

6. The figures on collision search are visually reassuring but methodologically thinner than the prose suggests. **Figure 4** shows boxplots for exhaustive continuation tests on the 10 closest prefix prompts, and the paper says “the boxplots look flat and uneventful, and that is the point.” I get the rhetorical intent, but this also highlights a limitation: the stress test is built on only 10 seed prompts selected from the closest observed cases in the sampled dataset. That is a reasonable diagnostic, not a comprehensive challenge set. I would have liked a more adversarial construction, for example prompts differing only by punctuation, whitespace patterns, repeated tokens, or templated program snippets, since the appendix later suggests such cases often produce the closest embeddings.

7. The inversion setting used for SIPIT is stronger than the most interesting threat model implied by the theory. Section 3 explicitly says that while the injectivity theorem guarantees exact recovery from the final embedding “in principle,” the algorithmic problem for that case is left to future work, and instead the paper assumes access to **all per-position states at a given layer $\ell$**. This is a meaningful relaxation. The causality-based sequential recovery in Equation (6) and Algorithm 1 depends crucially on having $\widehat{\mathbf h}_t$ for each position, not merely the final state. That does not invalidate SIPIT, but it substantially narrows the operational claim. The title and abstract could easily leave a reader thinking the paper provides a practical exact inverter from the final last-token state alone, which it does not.

8. The baseline comparison in Section 4.2 is not fully satisfying. **Table 5** compares SIPIT to HARDPROMPTS and a BRUTEFORCE ablation on GPT-2 Small. However, the paper itself admits on Page 8 and in Appendix E.1 that HARDPROMPTS is designed for a different setup and had to be adapted to the current setting by replacing its objective. Once that is the case, the comparison becomes much less informative as evidence that SIPIT is superior to prior inversion methods. The more relevant claim is that SIPIT is superior to brute-force search under the same access model, which Table 5 does show. But the framing against prior inversion literature is weaker than the table presentation suggests.

9. The quantization discussion is empirically interesting but theoretically muddy. On Page 8, the paper says quantization “does not introduce any collisions” and even “more than doubles the minimum distance between representations,” citing **Table 2** and **Table 3**. But earlier, the paper lists quantization among the kinds of deliberate non-analytic choices that can invalidate the theorem. So the current evidence should be framed as an empirical observation for specific FP4/INT8 implementations, not as any sort of support for the general theory. In fact, the quantized-model experiments underline that the assumptions are narrower than the headline claims, not broader.

10. The paper could do a better job positioning itself relative to adjacent inversion literature. The related work section mentions black-box inversion, prompt optimization, and the hidden-state recovery work of Thomas et al. (2025). That is a good start, but the novelty boundary around SIPIT still feels somewhat blurred: is the key novelty the proof of one-step injectivity, the exactness guarantee, or the candidate-ranking policy? The paper says “first algorithm that can recover the exact input sequence from hidden activations, with provable linear-time guarantees” on Page 10. That may be true under this exact access model, but the distinction from prior hidden-state inversion methods would benefit from a crisper apples-to-apples articulation in the main text.

11. There are a few presentation rough edges and inconsistencies that make the paper read more forcefully than precisely. For example, the method is referred to as “SIPIT,” “SipIt,” and “SipIt” in different places. The theorem numbering in the main paper is mildly awkward, with Theorem 2.3 followed by Corollary 2.3.1 and 2.3.2. The table numbering on Pages 7-9 is also confusing: Table 1 is referenced in the text, but the visible tables in the provided main text begin with “Table 2” and “Table 3,” then later “Table 4” and “Table 5” appear in an order that is easy to misread. These are fixable, but the paper is making subtle theorem-level claims, so exact presentation matters more than usual.

12. Some claims about significance spill beyond what is scientifically established by the paper itself. On Page 10 the paper argues that hidden states are “the prompt in disguise” and therefore any system storing or transmitting them is effectively handling the verbatim text. The spirit of that claim is understandable, and the paper rightly raises privacy concerns. Still, there is a jump from an exact recoverability theorem under a specific access model and assumptions, to broad legal and regulatory conclusions. Those implications deserve a more careful boundary between theorem, threat model, and policy interpretation.

## Questions
1. The most important clarification for me concerns **Theorem 2.3**. Can the authors state more precisely why the step-size restriction $\eta_t\in(0,1)$ is the right assumption? In the main text, the key property seems to be that $\det(I-\eta \nabla^2\mathcal L(\theta))$ is not identically zero, which is not obviously tied to the interval $(0,1)$ alone. A more explicit statement of the minimal condition would increase my confidence.

2. Please clarify the wording of **Theorem 2.1 / Equation (1)**. Do you mean: for each fixed discrete prompt $\mathrm s$, the map from continuous parameters and selected embedding variables to $\mathbf r(\mathrm s;\theta)$ is real-analytic? If so, I strongly suggest rewriting the theorem to avoid the phrase “jointly in the parameters and the input embeddings” while still displaying $\mathrm s$ as an argument of the map.

3. For **Theorem 3.2**, can you provide more empirical information about the distribution of $\Delta_{\pi,t}$ over sampled prefixes and positions, not just minima over prompt pairs? A histogram or percentile summary of empirical one-step margins would materially strengthen the connection between the robustness theorem and the observed practical success of SIPIT.

4. The practical access model of SIPIT assumes the full hidden-state sequence at layer $\ell$, whereas the theory in Section 2 is about last-token injectivity. Can you explicitly separate these two levels of claim in the abstract and introduction? Right now, a casual reader could easily conflate “invertible from final representation in principle” with “practically inverted by SIPIT under the same observation model.”

5. Regarding **Table 5**, do the authors have a stronger baseline under the same white-box hidden-state access model, or can they justify more carefully why HARDPROMPTS is a meaningful comparator despite being adapted from a different objective and setting? This matters because otherwise the strongest empirical comparison is really SIPIT versus BRUTEFORCE, which is useful but narrower.

6. **Figure 4** is based on 10 closest prefixes found in the dataset mixture. Could the authors add a more adversarially designed collision search in the main paper, for example prompts differing only by formatting, punctuation, repeated separators, or templated code variations? That would better stress-test the exact kinds of near-duplicate cases that seem most relevant.

7. The privacy implications are one of the most compelling aspects of the paper, but they also raise a scope question. Can the authors distinguish more explicitly between: (a) exact mathematical recoverability under their assumptions, (b) practical recoverability under exposed per-position hidden states, and (c) broader real-world leakage risks under finite precision, quantization, and partial access?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper studies exact prompt recovery from hidden activations and explicitly frames hidden states as potentially equivalent to user text for privacy purposes, especially in Section 3 and the discussion on Page 10. That creates a clear dual-use concern: the work is valuable for auditing and secure deployment, but it also provides a stronger theoretical and algorithmic basis for prompt reconstruction attacks if intermediate states or caches are exposed.

I do not view this as a reason to reject the paper, but it is worth ethics scrutiny because the operational message is that leaked KV caches, shared inference pipelines, or APIs exposing intermediate activations may enable exact recovery of private prompts. The paper acknowledges some of this, though a more explicit responsible-disclosure style discussion of attack surfaces and mitigations would be beneficial.

## Soundness Rating
3: good. The core theorem is interesting and the proof strategy appears substantial, but some of the strongest claims rely on assumptions and proof sketches that are not stated with enough precision in the main paper, especially around training preservation and the practical leap from exact injectivity to robust invertibility.

## Presentation Rating
3: good. The paper is generally readable and well organized, with strong intuition and useful figures, but several statements are stronger than necessary, some notation/theorem wording is imprecise, and the presentation would benefit from tighter calibration between theorem scope and headline claims.

## Contribution Rating
3: good. The theoretical framing is important and the combination of almost-sure injectivity with a constructive inversion algorithm is a meaningful contribution for the ICLR community, even though the operational scope of SIPIT is narrower than the title and abstract may initially suggest.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.

The paper has a real core idea, namely that for decoder-only Transformers viewed as maps from discrete prompts to continuous states, non-injectivity is generically a measure-zero pathology rather than the default. That is a worthwhile contribution, and the SIPIT construction makes the paper more concrete than a pure theorem paper. My hesitation comes from overbroad framing, the gap between exact injectivity and practical invertibility margins, and the fact that the empirical inversion setting is easier than the most interesting version of the problem. Still, I think the submission clears the bar.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I carefully checked the main arguments and experiments, but some appendix-level proof details are substantial enough that a full line-by-line verification would take more time.