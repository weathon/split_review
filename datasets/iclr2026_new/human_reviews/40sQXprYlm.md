## Human Reviewer 1

### Summary
The paper introduces Distributed Neural Architectures (DNAs), a new class of models where the computational graph is not fixed. The paper shows that DNAs, which are initialized with a set of modules (e.g., transformer, MLP) and routers, learn their own connectivity and computation patterns end-to-end. This architecture is presented as a natural generalization of sparse methods like Mixture-of-Experts (MoE) and Mixture-of-Depths (MoD). The authors train and evaluate DNAs in both the vision domain (on ImageNet, against a ViT-Small baseline) and the language domain (on Fineweb-Edu, against a GPT-2 Medium baseline).

On the positive side, the paper demonstrates that these models are competitive with their dense baselines in terms of performance. The primary contribution is a deep analysis of the emergent properties of these trained DNAs. On the negative side, there are some missing components, including a justification of the running time, and doing more in-depth analysis for vision vs. language tasks.

### Strengths
* The authors show that DNAs can learn to be compute-efficient by routing tokens to identity modules, and this compute allocation is interpretable (e.g., more compute is spent on visually complex images). This is interesting and seems to be novel.
* The authors also analyze the distribution of paths that tokens take (e.g., power law) and also that the learned modules can be interpretable in terms of their specializations. Frequent (low-rank) paths process high-level features like edges and flat colors, whereas infrequent (high-rank) paths are reserved for specific, low-level concepts 
* The paper considers both text and visual inputs, making it more general than just studying one modality.
* The analysis extends to the language models, considering punctuation and word pieces separately.

### Weaknesses
* There is high computational overhead of the proposed architecture. The authors admit that the current DNA implementation "runs slower and consumes more memory" than its dense baseline counterparts. This is attributed to the "unoptimized handling of dynamically changing sequence lengths" and the inability to precompute and cache attention masks. I think this makes it difficult to appreciate the practical benefit of "compute efficiency." The savings from skipping modules are currently outweighed by the overhead of dynamic routing.
* The performance is not a clear win; the paper aims for competitiveness, but the top-1 DNA language model achieves a worse validation loss (2.754) than the standard GPT-2 baseline (2.720). 
* Finally, the "fully distributed" concept is slightly compromised by empirical design choices required for stable training, such as hard-coding the first few layers as a non-routed "backbone".

### Questions
* It seems that optimization converges better when a hard-coded dense backbone ($N_b > 0$) is used to process all tokens before any routing begins. This seems to be a critical, un-ablated component that partially contradicts the core "fully distributed" premise. Does this finding imply that distributed routing is primarily effective as a refinement mechanism after a shared, dense feature extractor has processed the raw inputs? What happens if you try to force $N_b=0$ and compensate with other training techniques, such as a longer warmup or a different optimizer? If $N_b=0$ models fundamentally fail to converge, what does this tell us about the limitations of data-dependent routing at the earliest layers?

* Your results show a marked difference between vision and language domains. In vision, emergent parameter sharing is interpretable and correlates with image features (Fig. 7), and compute allocation is highly contextual (Fig. 5). In language, you conclude that parameter sharing is "most likely random" (Sec 4.3) and the performance gains are marginal (Table 3). Why do you believe this conceptual gap exists? Is it simply a matter of scale, where the 400M-parameter language model is too "underparametrized" for the complexity of FineWeb-Edu? Or, is it a fundamental mismatch, suggesting that a homogenous pool of Transformer blocks is less suited for language, which might require a more diverse "proto-architecture" of modules to learn meaningful, non-random specialization?

* The abstract states a token can "traverse any series of modules in any order," which implies a general, potentially cyclic, graph traversal. However, the implementation (Fig 1b, Sec 2.2) describes a "fully causal," step-based process where a router $R_s$ makes a decision at each step $s$ up to a maximum $s_{max}$. This step-based model appears to be less of a true "any order" graph and more of a deep, sequential MoE where the set of experts is simply the entire pool of modules. Could you clarify if it's possible for a token to be routed to module $M_5$ at step $s=3$ and then to module $M_2$ at step $s=4$? If so, how is this functionally different from just having two sequential routing layers? How critical is your specific $R_s$ implementation (a router-per-step) versus a more state-dependent design where each module $M_i$ has its own router that decides the next module?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper introduces distributed neural architectures which consists of attention, MLP, router modules. Each token or patch is learned to route among these modules end to end. The proposed architecture is competitive with dense models, and provides compute efficiency. Additionally, the routing paths of tokens among these modules is interpretable.

### Strengths
- Proposes a framework that generalizes most of conditional computation approaches used in training large models 
- Extensive analysis of routing paths of tokens to strengthen the fact that routing is interpretable 
- Results match dense baseline while being sparsely activated. 
- Experiments are comprehensive across vision and language modalities.

### Weaknesses
- Can you provide flops taken by the proposed method? It is hard to make comparison with baseline without flop comparison as their performances are similar.  Include it in the table which presents the results for each domain. 
- Learning routing is a hard problem faced in MoEs, MoDs. The proposed method doesn’t address it all, which makes the framework not useful at the current stage. 
- What’s the motivation to include skip identity modules? 
- Why does Top-2 DNA models always have skip modules in them and have different hidden size compared to others. It makes comparison harder. 
- Can you provide details about related works as to why this approach hasn't been successful in the past?
- Can you provide specific choices made to ensure the comparison of proposed method to baseline is fair?

### Questions
- Intuitively, it is mentioned that the higher rank path has a high frequency of tokens, while the lower is low frequency, how exactly is the rank computed? 
- The details on the architecture are somewhat unclear. Are there same modules at each step?  Is there a single router for each step?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces a novel neural architecture design paradigm called Distributed Neural Architectures (DNAs) and exhibits them in example vision and language modeling domains. The main motivation behind this paradigm is to allow the model to, via training, discover and organize itself into sparse paths which can be executed at inference time efficiently. DNAs are not feed-forward and allow information to flow between any pair of a set of computing modules. Each computing module is chosen as a piece of a Transformer such as MLP, attention, Transformer layer itself etc. In addition, there are routing modules whose job is to route a given set of input tokens to a given set of output modules. The routing is token-choice. DNAs are trained to allocate compute dynamically. The authors train a (i) classifier in the image domain on ImageNet, (ii) a generative model in the language domain using DNA.
The general proton-architecture of DNAs is as follows:
1. Input node (embedding layer)
2. Output node (unembedding layer)
3. N_m distinct computational modules
4. N_r distinct routers

The authors bias the model towards compute efficiency by using a bias term added in the router when routing to identity modules (or skip connections basically).
They observe the model chose interpretable paths and observe the emergence of contextual compute efficiency (i.e. different tokens/patches take different compute) and input-dependent parameter sharing (reuse of modules).

For the language task, they train GPT-2 sized models (with around ~400-500M parameters) on a subset of FineWeb-edu and obtain perplexity and downstream performance numbers similar to that of Transformer baselines.

### Strengths
- The paper proposes a novel and interesting paradigm for training neural networks. As pointed out in the paper, the main value of the paper is in proposing the paradigm and showing that it is feasible to train performant models in this paradigm. While they do not offer SoTA performance or practical wall-clock time efficiency with current hardware, it is an important research direction.

- The proposed DNA architecture could easily have ended up much less performant than the well-optimized Transformer. But the fact that the authors manage to get it to train to be reasonably performant is surprising and an indicator of the promise of the proposed approach.

### Weaknesses
- Even with current Transformer architecture, we achieve a high degree of sparsity via MoEs and efficient attention layers such as Mamba or sliding window attention. In addition, we can also achieve contextual sparsity in principle with methods such as early exit (Confident Adaptive Language Modeling Schuster et. Al. 22). It is unclear if there is evidence to believe that approaches like DNA can achieve a much sparser structure than these known methods.

### Questions
- An important question is whether there is a fundamental reason to believe DNAs can offer more efficient pathways compared to MoEs? Can you comment on this?
- Can you also provide mode details in the paper on how you implemented training and inference for the language generative task? You mention you can’t use the standard KV caches. Are there any other optimizations that can be done instead for DNAs?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes Distributed Neural Architectures (DNAs). DNAs use learned routers to let each token use the modules in flexible orders. Results show DNAs match dense baseline performance in vision and language tasks while learning interpretable, efficient compute allocation patterns that follow power-law distributions.

### Strengths
- This is an innovative work. The authors challenged the fixed architecture pipeline and proposed a genetic and flexible modular architecture.
- The authors come up with visualization designs to analyze the routing pattern of modular networks.

### Weaknesses
- Weak results: Evaluation results in vision tasks underperform the dense models. While the language task also show mixed results against the dense counterpart.
- Doubts on interpretability: As the authors also discovered, randomly initialized model also show some degree of "clustering". This cases doubt on the reliability of inspection the patches and read meaning from it. It may simply because the patches starts to be close to each other, and their representation remain close through out the layers, when those representation pass through the linear router, they naturally feel like having some "theme". Maybe rigorously determine whether a path have specialized on anything requires new analysis method, for example, mixing up paths from the proposed model and randomly initialized model, and then letting the researcher determine if there is any pattern without knowing the source.

### Questions
- Related works: https://arxiv.org/abs/2302.11529 has a lot of good related papers. Classical works like https://arxiv.org/abs/1511.02799 probably deserve a place. 
- This is an innovative work. But task performance is at an disadvantage, while the interpretability is not compelling enough. Potentially the compute saving may be an advantage. To prove this point, having two dense model baselines that have the same number of param as the total number of parameters, and active parameters can be helpful.
- Regarding the vision experiments, do you have datasets in mind that particularly can benefit from adaptive computation? Maybe the method isn't inherently weaker than dense model, just the datasets are mostly homogeneous.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4