---
job_id: d804a0b8-8239-40e2-97fe-d630ac1cf2e1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: NFB4QGGS65.pdf
paper: The Geometry of LLM Quantization: GPTQ as Babai’s Nearest Plane Algorithm
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining learning theory/geometry, optimization, and LLM post-training quantization for large-scale language models.

## Minimum Quality
Pass ✅. The paper contains the expected components, presents a clear technical thesis, includes formal results and empirical evaluation, and while I have several concerns about scope, exposition, and experimental breadth, I do not see a fatal flaw that would warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions to reviewers, or other signs of prompt injection or concealed review-targeting content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper gives a geometric reinterpretation of GPTQ for linear-layer quantization, showing that GPTQ, when run in reverse order, is equivalent to Babai’s nearest plane algorithm for a closest vector problem defined by a Hessian-derived lattice. Building on this equivalence, the paper derives a no-clipping layer-wise error bound, studies the role of quantization order, and proposes two practical no-clipping variants, SSQR and HPTQ, together with an SSQR CUDA inference kernel.

## Strengths
The main strength is the conceptual contribution. Recasting GPTQ as Babai’s nearest plane algorithm is a meaningful reframing of a widely used quantization method, and it does more than rename existing algebra. In particular, the connection between Eq. (2), Theorem 2, and Theorem 4 gives a coherent geometric interpretation of GPTQ’s error propagation that many practitioners will find useful.

The paper does a good job building intuition through figures. **Figure 1** is especially effective in showing how the partition induced by Babai differs from round-to-nearest and how ordering matters, which directly supports the paper’s later claim in Section 4.5 that quantization order affects the bound. Likewise, **Figure 2** helps translate the otherwise opaque OBQ/GPTQ update into a projection picture; this makes Theorem 2 much easier to parse than the raw algebra alone.

The theoretical story is fairly complete within its stated regime. The chain from Section 4.1 to Section 4.5 is logically structured: quantization as CVP, geometric meaning of OBQ, GPTQ-Babai equivalence, then a derived error bound. Even though some proof details are deferred, the main text presents a reasonably coherent arc rather than a pile of disconnected lemmas.

The practical angle is not purely ornamental. The no-clipping analysis leads to concrete schemes, HPTQ and SSQR, and the paper does not stop at theory. **Figure 4(a)** and **Table 3** show that HPTQ substantially improves over vanilla GPTQ and RTN in the very low-bit regime, especially at average bitwidth 3.125 and 2.125 on Qwen3-8B. For example, in **Table 3**, HPTQ at 3.125 bits achieves WikiText-2 perplexity 10.34 versus 12.77 for GPTQ and 10.75 for HRTN, which is a real empirical gain rather than noise-level movement.

The paper also includes systems relevance. The SSQR kernel and the speed results in **Figure 4(c)** give at least some evidence that the proposed representation is deployable, not just analytically neat. For an ICLR audience that increasingly cares about inference practicality, this is a legitimate plus.

## Weaknesses
1. **The theory is restricted to the no-clipping regime, while the paper’s central object, GPTQ, is most commonly used with clipping, and this limitation substantially narrows the practical force of the main guarantee.**  
   The core guarantee, **Theorem 5** on Page 8, explicitly assumes $\mathbb{Z}_{\dagger}=\mathbb{Z}$, and Section 5 itself acknowledges that original GPTQ clips and therefore violates the bound. This matters because the headline claim is not just an interpretation, but an imported error guarantee for GPTQ. In the regime many readers care about, namely fixed low-bit integer grids, the guarantee no longer applies. The paper is honest about this, but the practical message still ends up weaker than the framing suggests. Put bluntly, the paper proves something clean for a modified setting, then uses that to motivate new methods, but it does not resolve the setting that made GPTQ famous in the first place.

2. **The empirical evaluation in the main paper is too narrow relative to the ambition of the claims.**  
   The main text’s experimental presentation is almost entirely concentrated in **Figure 4**, with most quantitative evidence moved to the appendix. That is not automatically fatal, but here it weakens the case because the paper advocates practical new quantization schemes in addition to theory. In the main paper, the reader sees one perplexity plot on Qwen3-8B, one scaling plot for HPTQ, and one end-to-end kernel result. There is no main-paper ablation directly validating the theoretical ingredients, for example whether back-to-front order helps relative to front-to-back in the no-clipping regime, whether the LDL-derived bound correlates with observed error, or whether min-pivot improves downstream accuracy enough to justify the extra work. The appendix does include **Table 2** on $\operatorname{tr}(D)$, but this only partially addresses the issue, and the main-paper empirical narrative remains thin for an ICLR submission making both theoretical and practical claims.

3. **The comparison set is incomplete for a paper positioning HPTQ and SSQR as improved practical alternatives.**  
   In the main text, the comparisons in Section 5 are primarily against RTN, GPTQ, and HRTN, with SpQR discussed conceptually but not shown as a headline baseline in the main figures. This matters because SSQR is presented as a modification of SpQR-like outlier handling, and HPTQ is framed as a more practical no-clipping design. If the practical contribution is part of the acceptance case, then stronger direct empirical comparisons should be front-and-center. The appendix later includes comparisons to AQLM, QuIP#, and QTIP in **Table 16**, but again that evidence is not surfaced in the main narrative, and some of those results are pulled from prior papers rather than reproduced under a common setup. For a reader evaluating practical significance from the main paper alone, the evidence is less convincing than it should be.

4. **Several mathematical and notation issues in the main text create avoidable doubts about correctness and polish.**  
   There are multiple places where the notation appears broken or inconsistent. A particularly concerning example is in **Corollary 3** on Page 7, where the denominator appears as  
   $\left(X[:,J]\setminus X[:,J]\right)^{-1}[j,j]$,  
   which is clearly malformed and cannot be the intended quantity. Since the corollary is supposed to interpret OBQ’s dimension selection geometrically, such an error is not cosmetic, it interrupts the logic at a key point. Similarly, there are places where symbols for the integer domain vary, for example $\mathbb{Z}_{\dagger}$, $\mathbb{Z}_1$, and related notation in Section 4.1, which makes the clipped vs no-clipping distinction harder to track than necessary. For a paper whose main value is a careful equivalence proof, this level of notation sloppiness is unfortunate.

5. **The proof presentation in the main paper is too dependent on deferred appendix details, and some main-text theorems are stated with more confidence than the visible derivation supports.**  
   **Theorem 4** is the centerpiece, yet the “more rigorous algebraic proof” is explicitly deferred to Sections B and C. Likewise, **Theorem 5** has only a statement in the main text, with the proof entirely deferred to Section D. Deferring details is normal, but here the main text sometimes leans on theorems in a way that asks the reader to trust a long chain of nontrivial algebraic equivalences without enough local visibility. This is compounded by the fact that the appendix proof is lengthy and somewhat hard to audit due to notation overload. For example, the transition between LDL/UDU/Cholesky views across Algorithms 1, 4, 7, and 8 is mathematically plausible, but not especially transparent. A paper built around “mathematically identical” really has to be cleaner than this.

6. **The role of ordering is interesting theoretically, but the paper does not fully reconcile that theory with the practical algorithms it actually evaluates.**  
   Section 4.5 argues that back-to-front GPTQ aligns with Babai and that quantization order affects the bound through the LDL diagonal. Yet Section 5 states that “the quantization order is act-order for all methods.” This leaves an unresolved tension: the main equivalence is emphasized for reverse execution, but the practical methods are not evaluated in a way that isolates the effect of this theoretically privileged order. **Figure 1(h)** is useful precisely because it visualizes that changing order can change Babai partitions, but the experiments do not really capitalize on that insight. The appendix **Table 2** shows min-pivot reduces $\operatorname{tr}(D)$, but the main paper then says the downstream gains are modest without giving a substantial accuracy table in the main body. So the theory identifies an important lever, but the practical consequences remain underdeveloped.

7. **The practical methods are only loosely tied back to the theory, especially HPTQ.**  
   SSQR is at least motivated by avoiding clipping under limited budget, so the connection to Theorem 5 is understandable. HPTQ, however, moves to a global scalar scale with Huffman coding and an entropy-guided search, which feels more like a pragmatic coding scheme inspired by the no-clipping worldview than a direct consequence of the geometric results. That is not inherently bad, but the paper occasionally presents the applications as if they naturally fall out of the theory. In reality, the bridge is somewhat indirect. This affects scientific value because it blurs the line between what is theoretically implied and what is simply a reasonable engineering follow-up.

8. **Some claims around efficiency and deployment are underspecified in the main paper.**  
   The SSQR CUDA kernel result in **Figure 4(c)** is promising, but it is only compared against a PyTorch BF16 matrix multiplication baseline, under one hardware family and a narrow decoding setup. Since kernel engineering can look very different depending on batching, sequence length, and implementation baselines, the evidence is encouraging but not yet strong enough to support broad conclusions about deployment advantage. The appendix helps with **Figure 5**, but again, the main paper’s systems case is relatively light.

9. **The related-work positioning is good on older second-order quantization and lattice algorithms, but weaker on very recent geometry-aware quantization perspectives.**  
   The paper cites QuIP and related second-order PTQ works, which is appropriate, but the practical geometric landscape around LLM quantization has become broader, including rotation- or geometry-aware approaches that would help contextualize what is distinctive here. The omission does not invalidate the main claims, but it weakens the paper’s positioning. Since the pitch is partly “this opens the door to importing decades of lattice algorithms,” the authors should situate their geometric angle more explicitly against other geometry-based quantization strategies.

10. **There are a few exposition and pseudocode issues that make implementation fidelity harder to verify.**  
   For instance, in **Algorithm 10**, line 11 updates only $W[j,:]$ rather than the suffix $W[j:,:]$, which seems inconsistent with GPTQ-style propagation and likely a typo. Because the paper’s contribution rests heavily on algorithmic equivalence and practical variants, such pseudocode inconsistencies matter more than they would in a purely conceptual paper. They are fixable, but they reduce confidence in careful presentation.

## Questions
1. The main practical limitation is clipping. Can the authors sharpen the message around **Theorem 5** by quantifying, on the evaluated models, how often standard GPTQ actually violates the no-clipping assumptions and how strongly this correlates with the observed degradation in **Table 3** at 3.125 and 2.125 bits? A simple layer-wise statistic or histogram would help connect the theory to practice.

2. Can the authors provide a more direct empirical validation of the theory in the main paper, not only in the appendix? In particular, I would like to see one compact result comparing observed layer-wise error against the bound from **Theorem 5**, or at least against $\operatorname{tr}(D)$ under different orders.

3. The paper argues that reverse-order GPTQ matches Babai, but the practical methods use act-order. Did the authors test strict back-to-front execution versus act-order and min-pivot for the no-clipping variants? If so, please report downstream accuracy and not only trace-based proxies.

4. Please clarify the malformed expression in **Corollary 3** and audit the notation around $\mathbb{Z}_{\dagger}$ / $\mathbb{Z}_1$. These are important because the clipped versus unclipped distinction is central to the paper’s claims.

5. For **HPTQ**, can the authors explain more explicitly what part of the method is theoretically motivated versus heuristic? Right now, the entropy-guided binary search for a global scale reads as a practical design choice rather than something that follows from the Babai/CVP theory.

6. For the kernel results in **Figure 4(c)**, what stronger baseline should readers consider the most relevant comparison point in practice? If the answer is “our current comparison is only a first proof of feasibility,” saying that more plainly would improve calibration of expectations.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper. The work studies weight quantization and inference efficiency for public LLMs and uses standard public evaluation datasets. The main issues here are scientific clarity and scope, not ethics.

## Soundness Rating
3: good. The core technical claims appear broadly sound and the paper presents a credible theoretical argument, but the main guarantee applies only in the no-clipping regime and several notation/presentation issues make some details harder to verify cleanly.

## Presentation Rating
2: fair. The high-level narrative is understandable and the figures help, but the paper has enough notation inconsistencies, malformed expressions, and appendix dependence that the presentation falls short of what it should be for a theorem-driven submission.

## Contribution Rating
3: good. The GPTQ-Babai equivalence is a valuable conceptual contribution and the no-clipping variants are interesting, though the practical scope and empirical substantiation are not strong enough for a higher score.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper contains a real and useful theoretical insight, and the empirical results for HPTQ/SSQR are promising. At the same time, the practical relevance of the main guarantee is limited by the no-clipping assumption, and the paper needs a cleaner mathematical presentation and stronger empirical grounding to feel fully convincing.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the quantization/LLM compression context, though I did not independently re-derive every appendix proof line by line.