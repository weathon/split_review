## Human Reviewer 1

### Summary
This paper proposes an adaptive visual tokenizer that allocates a more optimal compressed sequence length than existing methods based on information theoretic principles. This paper demonstrates that prior works’ training methods are often suboptimal, imputing bias that makes the adaptive compressions lower-quality despite their adaptability. It further claims that the optimal design for the compressed token length should be proportional to the negative log likelihood of the input, and thus uses the learned ELBO to modulate the input compression factor. The proposed router uses this principle to more optimally allocate tokens for compression, and the top K tokens are selected based on their log likelihood. The results demonstrate that InfoTok achieves better performance at the same compression rates as comparable methods.

### Strengths
1) This paper provides some much-needed theoretical grounding to the adaptive tokenizer space, and attempts to pin down what `optimal’ adaptive compression should look like.

2) Experiments are very comprehensive and clearly demonstrate that InfoTok achieves better reconstruction at the same compression rate compared to other adaptive tokenizers.

3) While the results are incremental on their own, the entire paper is well structured and motivated, and properly places all the contributions in context, making the result valuable for the community.

4) While the claims in the theorems are initially hard to parse, they are empirically supported by experiments that make the intuition clearer.

### Weaknesses
1) Key definitions are not well highlighted in the text, and the mathematical sections are poorly written and hard to follow. Since definitions are missing from the theorems, the explanation is rather hard to follow. For example, the entropy H is not clearly defined, \mathbb{D} not defined. Similarly r(N | x) not defined in Alg 1 input. While I may have missed these definitions, I would suggest not burying them in the text and making key components clear and easier for readers to refer to.

2) It would be helpful if there were some visual results demonstrating the differences in InfoTok's reconstruction at different token lengths for the same image, so we could see what inputs are determined to need lower ones and which are determined to need higher ones. The reconstructions shown in Figure 2 are not particularly compelling - the compression results are considerably worse than Cosmos-DV.

3) There are no video samples provided in the supplementary material or project page which makes qualitative analysis of the results challenging.

### Questions
I don't have any strong suggestions, but would appreciate responses to my above critiques and would like to see them addressed in the next version of the paper.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes InfoTok, an adaptive discrete tokenizer that leverages an information-theoretic formulation to allocate token budgets based on the data's compressibility. The method introduces a principled way to determine token lengths using a normalized ELBO-based router and achieves strong empirical performance with a conceptually simple approach.

### Strengths
* The paper is well structured, and the mathematical formulation is precise.
* It achieves competitive or superior performance using a lightweight and interpretable mechanism.
* The authors provide rigorous justifications connecting ELBO with optimal token length, and the derivation is insightful.
* The ELBO-based routing and token selection reuse existing encoder-decoder structures and introduce minimal inference cost, which is appealing in practical deployments.

### Weaknesses
* Is the per-token ELBO computed purely based on the encoder-decoder’s end-to-end reconstruction path? Must this be explicitly introduced during training, or can the method be plugged into any VAE-style model without changes? Specifically, can non-VAE tokenizers be adapted to this framework?
* If N_max is small or the compression ratio is extremely low (e.g., β< 0.1), what are the observed effects on stability and convergence? Would the KL term dominate or explode in such settings, and does it impact model converging or generalization?
* The method is designed for videos. Would it generalize to other structured data types such as audio and 3D point clouds? Do different modalities affect the ELBO-based router's assumptions or effectiveness?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
In this paper, an algorithm called InfoTok is proposed for adaptive video tokenization. The proposed algorithm determines the token length based on ELBO for near optimal compression. For compression, InfoTok utilizes the ELBO based token selection. Thus, it can be integrated on the top of existing tokenizer architectures. Also, the proofs for the mathematical theorems are provided. The experimental results show that the proposed algorithm outperforms the existing methods.

### Strengths
- This paper clearly describes the proposed algorithm and is easy to follow.
- This paper provides the proofs for the theorems.
- The proposed algorithm achieves good performance on various benchmark tests.

### Weaknesses
- It would be helpful if the paper included a discussion of the limitations of the proposed approach. 
- Since the method seems general enough to be applied to images, it would be helpful to explain the rationale for limiting the experiments to videos.
- typo
  - L184: an more accurate -> a more accurate

### Questions
Though I have carefully reviewed the paper including the appendix, I did not observe any major drawbacks and I believe the proposed algorithm makes a meaningful contribution to adaptive video tokenization. Please see my minor concerns in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4