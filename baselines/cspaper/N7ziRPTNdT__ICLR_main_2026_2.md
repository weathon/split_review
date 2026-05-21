---
job_id: 35e684b9-7d12-4d18-bfef-567c54a6241d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: N7ziRPTNdT.pdf
paper: Generation Is Required for Data-Efficient Perception
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly in scope for ICLR, sitting at the intersection of representation learning, generative models, learning theory, causal/anti-causal generalization, and vision.

## Minimum Quality
Pass ✅ The paper contains the expected scientific structure, presents a nontrivial theoretical argument together with experiments, and is sufficiently complete and clear to warrant full review, even though I have important concerns about scope, empirical coverage, and some mathematical/presentation details.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies whether compositional generalization in data-efficient visual perception is better achieved by a generative approach, where representations are obtained by inverting a learned decoder, or by a non-generative approach, where an encoder directly predicts latents. The main claim is that under a particular structured function class for the true generator, the inductive biases needed for compositional generalization are straightforward to impose on decoders but generally infeasible to impose on encoders, especially in the realistic setting where images lie on a lower-dimensional manifold in ambient pixel space. Empirically, the paper evaluates encoder-based and decoder-based approaches on photorealistic PUG splits, and reports that generative methods using decoder inversion, via search and replay, substantially improve OOD compositional generalization relative to non-generative baselines unless the latter benefit from very large-scale pretraining.

## Strengths
1. The paper tackles an important question that is easy to phrase and genuinely relevant to ICLR, namely whether generation is actually required for data-efficient perceptual compositionality, rather than merely helpful. The framing around data efficiency and OOD compositional generalization is timely and sharper than generic “generative vs discriminative” debates.

2. The conceptual setup is unusually clean. Equations (2.1) to (2.6) make the distinction between identifying the forward generator \(f\) versus its inverse \(g=f^{-1}\) very explicit, and Figure 1 does a good job of visualizing the asymmetry the paper wants to establish. In particular, the left side of Figure 1 communicates the failure mode of an encoder that behaves correctly on observed combinations but maps unseen combinations incorrectly, while the right side illustrates why a structured decoder can still synthesize the OOD compositions. That figure is more than decorative, it is carrying the central intuition of the paper.

3. The theory section is ambitious and, within its assumptions, provides a nontrivial asymmetry argument. The contrast between the decoder-side regularity condition in Equation (3.1) and the manifold-dependent encoder-side condition in Equation (3.4) is the core technical point of the paper, and it is a meaningful contribution that this contrast is stated in a mathematically concrete way rather than as loose intuition. Theorem 3.2 is especially important because it formalizes the claim that when \(d_x \gg d_z\), local derivatives of \(g\) can be essentially arbitrary in ambient coordinates, undermining simple encoder-side regularization strategies.

4. The paper does a good job of connecting theory to implementable mechanisms. Section 4 does not stop at saying “invert the decoder” in the abstract, it proposes two practical routes, online search via Equation (4.3) and offline replay via Equation (4.4). Figure 4 is useful here: the left panel clarifies that search is initialized from the encoder and then refined under the decoder, while the right panel clarifies replay as encoder training on decoder-generated OOD compositions. That bridge from identifiability arguments to actual learning/inference procedures is a real strength.

5. The experiments, while limited in scope, are directionally aligned with the theory rather than feeling bolted on. Figure 5 shows a fairly coherent pattern across the three PUG splits: weak OOD performance for many non-generative methods on PUG-Background, somewhat better performance on PUG-Texture, and near-ceiling behavior on PUG-Object where the paper’s easier \(n=0\) special case applies. The contrast across panels A/B/C is a nice empirical sanity check on the theory’s claim that interaction structure matters.

6. Figure 6 reports substantial improvements from replay and search for the generative pipeline. In panel A, the stacked bars make clear that replay contributes a large part of the gain and search adds a further bump; that visual presentation supports the paper’s claim that decoder inversion is useful both offline and online. Even without a results table, these figure-based summaries are readable and informative.

7. The paper is generally well written for a theory-plus-experiments submission. The main ideas are understandable without needing to dig through the appendix, and the discussion section is reasonably candid about limitations of the diffeomorphism and interaction assumptions.

## Weaknesses
1. The headline claim is stronger than what the paper really establishes. The title says “Generation Is Required for Data-Efficient Perception,” but the actual theoretical results are proved only under a very specific modeling pipeline: images are generated by a diffeomorphic \(f \in \mathcal{F}_{\text{int}}\), perception is defined strictly as inversion up to slot-wise bijections/permutations via Equation (2.1), compositional OOD regions are Cartesian products as in Equation (2.4), and guarantees are discussed relative to exact or approximate membership in \(\mathcal{F}_{\text{int}}\) or \(\mathcal{G}_{\text{int}}\). That is a much narrower statement than the title suggests. This matters because many readers will take the title as a broad claim about visual learning in general, while the paper actually proves a claim about one particular formalization of perceptual compositionality.

2. The practical gap between the theory and the implemented decoder is under-addressed. Section 3 argues that decoders can be constrained to \(\mathcal{F}_{\text{int}}\) “in a straightforward manner,” via architecture or regularization, using Equation (3.1) or the regularizer in Equation (3.2). But the actual experiments in Section 5 do not use a decoder that explicitly enforces Equation (2.7), nor do they regularize higher-order derivatives directly. Instead they use a regularized cross-attention Transformer decoder motivated by Brady et al. (2025). That may be a reasonable approximation, but the paper’s practical conclusion depends on how faithful that architecture is to the theoretical class. Right now the chain of logic is looser than the prose suggests: the theorem is about \(\mathcal{F}_{\text{int}}\), the implementation is only argued to be “designed according to” that structure. This matters because if the empirical gains come from a broader set of design choices than the theory captures, then the central explanatory claim is less secure.

3. The empirical comparison is not yet strong enough to support a broad negative statement about non-generative methods. The main benchmark family in Section 5 uses PUG splits, which are photorealistic but still controlled and relatively small. The results in Figure 5 are suggestive, but they compare a somewhat heterogeneous collection of pretrained base encoders, optional LoRA tuning, and slot encoders, then report the best-performing combination for each base encoder. That is useful as an exploratory sweep, but it is not a decisive test of whether encoder-only methods fundamentally fail, or whether the chosen object-centric bottleneck and training setup are simply not the best form of encoder-only modeling for these data. Since the paper’s theoretical target is broad, stronger empirical evidence would be needed to rule out alternative encoder-side inductive biases or training procedures.

4. The treatment of optimization and model selection in the experiments leaves important ambiguities. On Page 8, for each base encoder the paper reports “the OOD accuracy obtained with the best-performing combination of slot encoder and fine-tuning choice.” It is not specified in the main paper whether that “best-performing” choice is selected using a validation split that excludes OOD test labels, or whether it is effectively chosen post hoc from OOD outcomes. If the latter, the reported OOD performance is optimistic. Similarly, for search in Appendix B.3, learning rates, iteration counts, and entropy regularization weights are given as sets of candidate values, but the selection protocol is not described in the main paper. This matters because OOD compositional generalization is precisely where evaluation can be accidentally biased by tuning on the test condition.

5. The mathematical exposition has several points that are too compressed or slightly inconsistent for a paper whose contribution relies heavily on formal statements. A concrete example is in Section 2, where \(\phi\) is introduced as \(\phi:\mathbb{R}^{d_z}\to\mathcal{Z}\) although it is supposed to map images \(x \in \mathcal{X} \subset \mathbb{R}^{d_x}\) to latents. That should presumably be \(\phi:\mathcal{X}\to\mathcal{Z}\) or \(\phi:\mathbb{R}^{d_x}\to\mathcal{Z}\). There is a similar mismatch on Page 3 where the generative decoder is written as \(\hat f:\mathcal{Z}\to\mathbb{R}^{d_z}\), although the codomain should be image space, not latent space. These are not just typos in a purely expository paper, because the main argument hinges on carefully distinguishing maps between latent space, manifold image space, and ambient image space.

6. Some of the central mathematical claims are plausible but not fully digestible from the main paper alone because too much of the actual mechanism is delegated to the appendix. Theorem 3.2 is central to the argument that local encoder-side regularization in ambient coordinates is futile when \(d_x \ge d_z^3\). But in the main text, the intuition for why the threshold \(d_x \ge d_z^3\) appears, and how strong the “almost every \(A\)” qualifier is, is minimal. The appendix helps, but the main paper could better explain the parameter counting and whether \(d_z^3\) is a proof artifact or believed to be near-tight. This matters because otherwise the result reads as a strong impossibility statement with opaque constants and assumptions.

7. The empirical results do not disentangle how much of the gain is due to “generation” per se versus extra computation, test-time optimization, and auxiliary classifier-based regularization. For search, the optimization in Appendix B.3 adds not only decoder inversion under Equation (4.3) but also an entropy regularizer on classifier logits. That means the search procedure is not a pure implementation of generative inversion, it also uses downstream label-structure priors through the classifier. Likewise, replay adds generated data and extra encoder training. These interventions are reasonable, but then the paper should be more careful about attributing the entire improvement in Figure 6 to the generative principle alone. This matters because the comparison is not computationally or algorithmically matched to the encoder baselines.

8. The paper does not provide enough ablation on decoder structure and inversion mechanics in the main body. Appendix C includes one comparison between a structured Transformer decoder and an unstructured CNN decoder, and Figure 9 is directionally useful, but this evidence is outside the main paper. Given that the theoretical message is specifically about the importance of the decoder’s structural constraints, one would expect the main paper itself to contain an ablation over decoder regularization strength, structured versus unstructured decoding, search initialization quality, number of search steps, and replay distribution design. Without that, the causal link between theory and empirical gain remains somewhat asserted rather than demonstrated.

9. The paper’s use of the \(n=0\) PUG-Object result in Figure 5C is suggestive but somewhat overinterpreted. The near-perfect OOD generalization there is used to support the claim that stronger structure on \(\mathcal{G}_{\text{int}}\) makes encoder-side compositionality easier. That may well be true, but PUG-Object also differs from the other splits in practical ways beyond the formal \(n=0\) assumption, including the nature of the compositions and the visual interactions. The paper would be stronger if it more carefully isolated what aspect of the split is responsible for the easy OOD performance, rather than reading Figure 5C as a fairly direct confirmation of the theory.

10. There is no explicit quantitative accounting of the computational tradeoff in the main paper, even though the paper advocates search and replay as practical routes. Appendix D gives rough timing numbers, but the main text does not discuss whether the OOD gains in Figure 6 are worth the added cost, or how these methods would scale with more complex decoders and higher-resolution images. Since the practical punchline is that generation is required, the cost of using it is not a side issue.

## Questions
1. Please clarify the exact model-selection protocol for the results in Figure 5 and Figure 6. When you report, for each base encoder, the “best-performing combination of slot encoder and fine-tuning choice,” what dataset or split is used to choose that combination? If any OOD labels were used, even indirectly, that would substantially weaken the empirical conclusions.

2. Relatedly, how were the hyperparameters for search selected, specifically the number of optimization steps and the entropy regularization weight described in Appendix B.3? A clean answer here would materially increase confidence in the OOD results.

3. Can you sharpen the scope of the main claim in the title and abstract? I would like to understand whether you are claiming necessity only within the formal setup of Equations (2.1) to (2.7), or whether you believe the result extends beyond \(\mathcal{F}_{\text{int}}\). If it is the former, the wording should probably be toned down.

4. How close is the regularized cross-attention Transformer decoder used in Section 5 to membership in \(\mathcal{F}_{\text{int}}\)? Even a qualitative argument or diagnostic would help. For example, can you measure whether cross-slot higher-order interactions are actually suppressed in the learned decoder in the way suggested by Equation (3.1) or its higher-order analogues?

5. Can you provide a stronger main-paper ablation on decoder structure? The appendix comparison to an unstructured CNN is a good start, but the central claim would be much more convincing if the main paper directly showed how OOD gains degrade as decoder structure or regularization is weakened.

6. In Equation (3.4), the manifold-dependent encoder constraint is the technical heart of the asymmetry argument. Could you add more intuition in the main paper about why this dependence on \(\Pi_{T_x\mathcal{X}}\) makes practical regularization ill-posed, beyond the brief prose currently provided? In particular, it would help to explain whether approximate tangent estimation from ID data could plausibly rescue an encoder-side approach, or whether your theorem rules out that hope more fundamentally.

7. For the \(n=0\) special case discussed on Page 5 and evidenced by Figure 5C, can you better separate the formal explanation from dataset-specific convenience? A targeted synthetic ablation varying only interaction structure would strengthen that part of the story.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The experiments use synthetic/controlled photorealistic data and the paper does not introduce obvious privacy, safety, or fairness risks beyond standard concerns about overclaiming generality from controlled benchmarks.

## Soundness Rating
3: good. The central technical argument is thoughtful and mostly coherent, and the experiments are aligned with the paper’s claims, but there are meaningful caveats about the scope of the theory, implementation-theory mismatch, and evaluation protocol details.

## Presentation Rating
3: good. The paper is generally well organized and readable, with effective figures such as Figures 1, 4, 5, and 6, but there are several notation/type inconsistencies and some central technical points are compressed too aggressively in the main text.

## Contribution Rating
3: good. The paper makes a meaningful contribution by articulating and empirically probing an asymmetry between decoder-side and encoder-side inductive biases for compositional generalization, even if the empirical scope and generality of the conclusions are narrower than the title suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a strong core idea, an interesting theoretical asymmetry, and empirically supportive results, especially in Figures 5 and 6. At the same time, the scope of the claim is overstated, the experimental evidence is not yet decisive enough to justify broad conclusions about non-generative perception, and several mathematical and evaluation details need clarification. I lean positive because the central argument is substantive and worth discussion at ICLR, but this is not an easy accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant representation learning and identifiability literature, though some proof details in the appendix would still benefit from author clarification.