Now I have a thorough understanding of both the paper and the review inputs. Let me write the consolidated review.

## Summary

This paper proposes L2C (Learning to Complement), a method for Few-Shot Test-Time Domain Adaptation (FSTT-DA) that extends the VDPG framework. L2C introduces a parallel network (CPNet) that learns dataset-specific knowledge to complement frozen CLIP's generalized features, a greedy text ensemble procedure to sharpen class prototypes, and a domain-aware fusion mechanism that adapts both visual and text features toward unseen target domains. Experiments on five benchmarks (WILDS and DomainNet) show consistent improvements over VDPG and other baselines, with particularly strong gains on the more challenging WILDS datasets using the weaker ViT-B/16 backbone (e.g., +5.1 F1 on iWildCam, +3.1% WC Acc on FMoW).

## Strengths

1. **Clear and measurable performance gains over strong baselines**: The method substantially outperforms the prior state-of-the-art (VDPG) across multiple challenging benchmarks, with the largest gains occurring precisely where they are most needed — on difficult real-world distributions (iWildCam, FMoW) using a weaker backbone (ViT-B/16). These improvements are documented in Table 1 and Table 2 across 5 datasets and two backbone sizes.

2. **Well-validated component design via ablation**: Each proposed component (CPNet, revert attention, text refinement, greedy ensemble, uniformity loss, domain-aware fusion, domain-centric training) is ablated in Table 3, showing that each contributes positively to the final performance. This gives confidence that the design is purposeful rather than over-engineered.

3. **Insightful problem framing — complementing CLIP rather than fine-tuning it**: The paper correctly identifies a limitation of VDPG: relying solely on CLIP's frozen feature space binds the method to CLIP's prior knowledge, which is insufficient for downstream datasets CLIP has not seen. Adding a lightweight parallel network that learns dataset-specific information from the image input (as opposed to CLIP's output features) is a principled and practical approach that preserves CLIP's OOD capabilities while augmenting them where needed.

4. **Greedy text ensemble is a simple and effective contribution**: The pre-processing step that selects prompt templates maximizing inter-class uniformity is clean, computationally negligible (text encoder discarded after preprocessing), and validated to improve performance across benchmarks (Table 6) with a clear supporting analysis (Figure 6 showing correlation between lower uniformity and higher accuracy).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Imprecise characterization of CPNet's input processing**: The paper repeatedly states that CPNet "learns directly from the input space" (Abstract, Sec. 1, Sec. 4.1), contrasting this with VDPG's approach of operating on CLIP's output features. Section 4.1 describes the input as an image that is "first split into *l* patches and encoded into embeddings with dimension *d*" — but it never specifies whether this encoding is performed by a separate patch embedding layer (making CPNet genuinely independent of CLIP) or by CLIP's own patch embedding. The "input space" vs. "feature space" contrast is conceptually valid regardless (CPNet processes images, not CLIP's output features), but the ambiguity invites confusion. Given that CPNet is described as "independent" and "in parallel," the natural reading is that it has its own patch embedding, but the paper should state this explicitly. This is a clarity issue, not a methodological flaw — the claim does not amount to "CPNet processes raw pixels" as the reviewer asserts, but it could be stated more precisely.

2. **Revert attention mechanism lacks analytical depth**: Equation (1) defines *A* = **1** − softmax(**CP**(*x*^in) · **I**(*x*^in)), which downweights positions where CPNet and CLIP produce similar representations and upweights positions where they differ. The paper does not specify which dimension softmax is applied over (presumably the last/token dimension in the standard attention fashion), and provides no analysis of what the attention maps look like after training, how they evolve, or whether the mechanism actually produces decorrelated/orthogonal features between CPNet and CLIP. The ablation (Table 3, Index 4 vs. 5) shows that removing RT hurts performance, which is evidence that it contributes, but not evidence that it achieves the stated goal of "focusing solely on information distinctive from CLIP." This does not invalidate the method given the empirical support, but it leaves the mechanism's theoretical grounding weaker than it could be.

### Trivial

1. **Softmax dimension ambiguity in Eq. (1)**: The paper should specify along which dimension the softmax is computed in *A* = **1** − softmax(**CP**(*x*^in) · **I**(*x*^in)), as this affects the interpretation of the resulting attention map.

## Nice-to-Haves

- A small diagnostic experiment for the revert attention mechanism, such as measuring the cosine similarity or mutual information between CPNet features and CLIP features with and without RT, or visualizing attention maps on a few examples, would strengthen the claimed "complementary learning" narrative.
- An explicit statement of whether CPNet uses its own patch embedding or shares CLIP's, along with an ablation comparing the two, would resolve the "input space" ambiguity.

## Removed Points

The following points from the Harsh Reviewer have been removed:

1. **"Text encoder can be discarded" phrasing criticism**: The reviewer claimed the refinement module (Eq. 4) "still requires text features during training on source data" contradicting the statement that the encoder "can be discarded when training starts." This is incorrect — the refinement module operates on the already-ensembled text features **T**^gre (obtained as preprocessing), not on the text encoder itself. The paper is accurate on this point.

2. **"Domain token attends to all patches or long sequence" confusion**: The reviewer stated it is "unclear whether the domain token attends to all patches from all images or whether the patches from different images are treated as a long sequence." The paper clearly states: it reshapes the batch to combine dimensions into **x̃**^e ∈ ℝ^{1×(b×l)×d} and prepends a domain token that attends to the entire sequence. These are the same thing — all patches from all images treated as a single long sequence. The description is unambiguous.

3. **"Input space" criticism framed as CPNet using "CLIP's own patch embedding layer"**: The reviewer asserts as fact that CPNet uses "CLIP's own patch embedding layer" and that the "input space" claim is therefore an overstatement. The paper does not state this. It describes the image being "split into patches and encoded into embeddings" without specifying whose encoder performs this step, and explicitly describes CPNet as "independent" and running "in parallel." The term "input space" is used correctly to contrast with VDPG's "feature space" (CLIP's output features). The ambiguity about whether CPNet has its own patch embedding is a real clarity issue (kept as Minor Weakness #1 above), but the reviewer's characterization of it as a "nontrivial overstatement" of the contribution is unwarranted.

## Novel Insights

The most interesting observation from the review process is that the paper's strongest results come precisely in the setting where its design philosophy matters most: with a weaker backbone (ViT-B/16) on challenging real-world domains. VDPG's approach of "stay entirely in CLIP's feature space" works well enough when CLIP is large (ViT-L/14) but collapses on harder distributions with a smaller model. L2C's explicit mechanism for learning dataset-specific knowledge outside CLIP's frozen representation creates a robustness that is backbone-agnostic. This suggests that for FSTT-DA, the marginal value of additional dataset-specific learning capacity is highest precisely when the foundation model's own capacity is limited — a finding that could inform future system design even beyond the specific components proposed here.

## Suggestions

1. Clarify in Section 4.1 whether CPNet uses its own patch embedding layer or shares CLIP's, and state explicitly what "learning from the input space" means operationally.
2. Add a brief note specifying the softmax dimension in Eq. (1) (e.g., "softmax applied along the last dimension") to avoid ambiguity.
3. Consider adding a small analysis of the revert attention mechanism — even a simple figure showing mean attention weights for a few patches or a correlation analysis between CLIP and CPNet features with/without RT would significantly strengthen the paper's claims about complementary learning.
4. The greedy text ensemble is clean and well-validated; consider moving some of its methodological detail to the appendix to free space for the clarifications above.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>