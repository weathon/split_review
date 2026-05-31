## Summary
The paper introduces **Diffusion-free SCORE matching (DISCO)**, a method for training a single, time-independent score function that approximates the score of the (slightly perturbed) data distribution. Unlike diffusion models that learn a family of time-indexed score fields, DISCO uses a weighted mixture of Fisher divergences over various noise levels to ensure the score is learned both on and off the data manifold. The primary motivation is to enable **exact conditional sampling** for probabilistic reasoning, which is notoriously difficult in diffusion models because the conditioning information is typically only available for clean data.

## Strengths
- **Principled Framework:** The paper provides a solid theoretical derivation (Theorem 1) showing that the DISCO loss has the same gradients as a weighted mixture of Fisher divergences. This bridges the gap between classical denoising score matching and the robust training benefits of diffusion.
- **Probabilistic Fidelity:** The method addresses a significant pain point in generative modeling: the inability of diffusion models to perform sound Bayesian inference. By learning a single joint score $\nabla_{\mathbf{x}} \log p(\mathbf{x})$, conditioning becomes a simple matter of clamping observed variables.
- **Strong Empirical Results:** DISCO demonstrates competitive performance against state-of-the-art diffusion models (EDM) on standard benchmarks like CIFAR-10 and FFHQ-64 in terms of FID, while significantly outperforming them on conditional sampling tasks (inpainting) and low-dimensional density estimation.
- **Clarity of Motivation:** The paper clearly identifies why diffusion models struggle with conditioning (the need for $\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t | \mathbf{x}_0^c)$) and provides a clean alternative.

## Weaknesses
### Fatal
None.

### Major
- **Scalability of Posterior Sampling:** The training objective requires sampling from the posterior $p_0(\mathbf{x} | \mathbf{x}_t)$. While the authors suggest a mini-batch approximation or nearest-neighbor search, this introduces a dependency on the training set size or batch size. In very large-scale datasets (e.g., ImageNet), the mini-batch approximation might become high-variance or biased if the batch doesn't contain samples sufficiently close to the perturbed $\mathbf{x}_t$.
- **Masked Training Dependency:** The authors note that in high dimensions, the basic DISCO loss fails to learn accurate scores for conditional sampling, necessitating a "Masked DISCO" variant. This suggests that the "diffusion-free" nature of the joint score isn't quite enough to capture the manifold structure for arbitrary conditionals without explicit task-specific augmentation (masking).

### Minor
- **Sampling Speed:** While DISCO avoids the time-indexed score fields, the sampling still requires iterative methods (Heun, SMC, or HMC). The paper uses a similar number of steps (NFE) as EDM. It would be beneficial to clarify if DISCO offers any inherent sampling speedup or if it is purely a fidelity/inference play.
- **Comparison to Consistency Models:** While the paper compares to many diffusion heuristics, it doesn't discuss Consistency Models, which also aim to map noise to data in fewer steps, though they don't solve the exact conditioning problem in the same way.

### Trivial
None.

## Nice-to-Haves
- A more detailed ablation on the effect of the mini-batch size used for the posterior $p_0(\mathbf{x} | \mathbf{x}_t)$ approximation.
- Evaluation on non-image inverse problems (e.g., sparse sensing) to further prove the "probabilistic reasoning" claim.

## Novel Insights
The core novel insight is the re-interpretation of the "diffusion" noise levels not as a temporal process to be reversed, but as a set of **proposal distributions** for a weighted Fisher divergence objective. This allows the model to inherit the training stability of diffusion (learning the score far from the manifold) without the "latent variable" baggage that makes exact conditioning intractable. The paper correctly identifies that the time-dependency in diffusion is a hindrance to standard probabilistic operations like marginalization and conditioning.

## Suggestions
- In the final version, provide more intuition on the choice of $\gamma$ in the masked loss and how sensitive the FID/Inpainting results are to this hyperparameter.
- Clarify the computational overhead of the posterior sampling step during training compared to standard EDM training.

## Score and Decision
The paper is well-written, theoretically grounded, and addresses a fundamental limitation of the current generative modeling paradigm. The results on conditional sampling are particularly compelling.

MY FINAL SCORE: 8.0
MY FINAL DECISION: Accept