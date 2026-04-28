# LOB-Bench: Benchmarking Generative AI for Finance - with an Application to Limit Order Book Markets

- Decision: Reject
- Avg Score: 3.33
- Scores: 6, 1, 3

## Abstract
We present **LOB-Bench**, a benchmark designed to evaluate the quality and realism of generative message-by-order data for limit order books (LOB). We enable a rigorous and comprehensive model comparison by providing both a theoretical framework and an open-source Python package. Addressing the lack of consensus on evaluation paradigms in the literature, where qualitative comparison of stylized facts is prevalent, our work offers a crucial building block for advancing generative AI for financial data. LOB-Bench provides a standardized method to numerically assess the quality of various model classes that generate limit order book data in the widely used LOBSTER format. It provides a range of quantitative characteristics and includes a simple parametric benchmark model as a baseline. Our framework measures distributional differences in conditional and unconditional statistics between generated and real LOB data, supporting a flexible multivariate statistical evaluation across different model classes. The benchmark features commonly used LOB statistics such as spread, order book volumes, order imbalance, and message inter-arrival times, along with adversarial scores derived from a neural network trained to differentiate between real and generated data. Additionally, LOB-Bench evaluates "market impact metrics" by computing cross-correlations and price response functions for specific events in the data. We present empirical benchmark results for a generative autoregressive state-space model, for a (C)GAN, and parametric LOB model. We find that the autoregressive GenAI approach beats traditional model classes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents the LOB-Bench, a benchmark designed to evaluate the quality and realism of generative models for Limit Oder Book(LOB) data. It provides a theoretical framework and Python package that systematically compares generative models like autoregressive models, (C)gAN, and agent-based models. It uses a range of metrics like spread, order book volumes, order imbalance, and adversarial scores to asses the distributional differences between generated and real LOB data. Empirical results demonstrate that the autoregressive generative approach outperforms traditional models, offering a standardized evaluation for financial data generation.

### Strengths
1) The paper proposes unconditional and conditional evaluations, allowing for a nuanced comparison of generative models. It accounts for model drift and evaluates market impact metrics, making the framework robust.

2) The use of widely adopted LOBSTER data for empirical evaluations makes the benchmark relevant for practitioners in the financial domain.

3) The open-source code enhances the reproducibility and practical unity of the work.

### Weaknesses
1) The paper explores generative models; some more, like advanced deep learning architectures, could be explored. Specifically, the benchmark could benefit from including models that explicitly capture the temporal dependencies in LOB data, such as transformer-based architectures, which have shown promise in other sequence modeling tasks. The current selection of models, while relevant, might not fully represent the state-of-the-art in generative modeling for time series data.
2)  The evaluation highlights that errors accumulate over longer sequences. The benchmark does not fully address how to mitigate this. The accumulation of errors in long sequences is a critical issue, particularly in financial time series where long-range dependencies can significantly affect market dynamics. The benchmark should include methods for evaluating and mitigating this error accumulation, such as techniques for sequence-level error correction or methods that explicitly model long-range dependencies.
3) Certain model results with rate events like market orders have data sparsity. and generating additional data might not be practical. The issue of data sparsity, particularly with rare events such as large market orders, poses a challenge for generative models. The benchmark should include methods for evaluating model performance under such conditions and explore techniques for data augmentation or synthetic data generation that can address this sparsity.

### Questions
1) The framework does not account for hidden liquidity, which is critical for LOB modeling. The model can be improved in this area. 
2) Why did you focus on autoregressive models, (C)GANs, and agent-based models? Have you considered other deep learning architectures for LOB data generation, such as transformers or diffusion models?
3) Could you clarify why you selected the L1 and Wasserstein-1 distances as the primary metrics for distributional comparison? How do these metrics handle the complexities of financial time series data, such as fat-tailed distributions or volatility clustering?
4) The benchmark evaluates market impact metrics, but how do you account for outliers or extreme events in real-world LOB data? Are these adequately captured in your current framework?
5)  The conditional evaluation approach looks at conditional distributions of specific LOB statistics. How would this framework perform when dealing with very high-dimensional data, and does it scale well for more complex scenarios?
6) The paper uses the LOBSTER dataset for evaluation. Given its limitations (e.g., limited asset coverage, certain missing features), do you think the results would generalize to other datasets or more diverse market conditions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper proposes a unified benchmark framework, LOB-Bench, designed to quantitatively evaluate generative AI models with a focus on limit order book (LOB) data. Unlike prevailing qualitative measurements, this framework provides numerical results to analyze the accuracy of how the LOB generative models resemble the real data. Compared to current quantitative metrics in the literature, such as cross-entropy, LOB-Bench is claimed to better deal with issues like distribution shifts and autoregressive gaps within data. LOB-Bench is applied to evaluate a range of generative models. The experiment section presents some interesting findings. Specifically, the results indicate that autoregressive GenAI’s excel in learning LOB data more effectively than traditional methods.

### Strengths
1. This paper highlights the essential demands for quantitative metrics to evaluate generative AI for finance and addresses this critical problem by introducing several innovative quantitative metrics, which are well-motivated and useful for the further development of generative AI in finance.
2. This paper effectively employs visualizations to show the quantitative results, making them intuitive and comprehensive for a broad audience.

### Weaknesses
1. This paper provides a non-anonymous code link on line 097, which violates the double-blind protocol of the conference. The authors should take care to remove or anonymize the link for the review process. 
2. This paper displays several signs of incomplete editing that require further proofreading. Specific issues include a non-functional GitHub link on line 033, and repeated sentences between lines 097-099. Before submitting, the authors should conduct a thorough proofreading pass, paying particular attention to consistency in links and removing any redundant text. 
3. Although the paper introduces a new benchmark for evaluating generative AI models, it does not adequately compare this benchmark with existing alternatives. Furthermore, the experiments fail to convincingly demonstrate the benchmark's claimed ability to effectively address distribution shifts or autoregressive gaps within the generated data. What are some existing benchmarks against which the proposed method can be compared against? Specific experiments that clearly demonstrate superiority in dealing with distribution shift or autoregressive gaps in the generated data would make the method more convincing.

### Questions
1. As mentioned above, this paper does not demonstrate that LOB-Bench addresses autoregressive gaps and distribution shifts effectively. Can you provide a detailed analysis or case studies that illustrate the benchmark's performance in managing these specific challenges?
2. Could you demonstrate how LOB-Bench differentiates between generated and real LOB data in certain scenarios where traditional methods such as cross-entropy fail to?
3. How does the proposed benchmark influence the development and refinement of generative AI models? Are there examples where insights derived from LOB-Bench can directly lead to improvements in model architecture or training methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The gist of the paper is to evaluate the realism of generated LOB orders. In more detail, the authors want to numerically assess the quality of the generated data instead of just using stylized facts, classic LOB evaluation format, nor only cross-entropy, usually used in generative approaches. The authors want to evalute pre-trained models in *sampling regime*.

### Strengths
The paper presents some interesting ideas about evaluating autoregressive models by binning the generated order into some aggregation function $\Phi$ to avoid accumulating errors in time. The quantitative evaluation metric is the L1 distance between $p(x)$ and $\hat{p}(x)$. What this means is still a mystery to me and I'd appreciate to have more clarification from the authors here.

### Weaknesses
### Discussion over the meaning of L1 as a qualitative evaluation metric
I appreciate the authors taking the effort of running all stylized facts experiments and stress-testing 2 SoTA and 1 baseline method. However, the authors claimed in the beginning that just having stylized facts, already thoroughly explored by Vitrienko et al. [5], isn't sufficient. While they support this claim by introducing the L1 as a qualitative metric, it lacks substance and overpresenting these stylized facts overshadows the "novelty" of the benchmark. Anyhow, to the best of my understanding, the L1 should quantitatively say how good a LOB generation model performs. Nevertheless, I argue that it'd be simpler and more than enough to train a model -- even a simple one -- on a financial downstream task -- say mid-price prediction -- on "fake" generated orders and measure its MSE. Then, at test time, one would measure the model's MSE on real orders and see how well the model trained on generated orders generalizes over the real data. This would be a sufficient indicator to assess the goodness and realism of the generated data. Furthermore, you wouldn't even need to bin your data and go through unnecessary hoops just for the sake of the benchmark. So, the question raised here is *Why is the literature in LOB generation "dying" to have your contribution? What are you bringing to the table that future works are going to benefit from?*

### Shortsightness and lack of discussion within the benchmark
As a benchmark paper, I would expect the authors to give insights and directions for future autoregressive/generative LOB models. This is lacking which undermines its usefulness. Again *What is it that future researchers would benefit from this benchmark?*

### Weaknesses
1. **Why did you share your GitHub repository not anonymized? Now, I know your identity and have reported it to the ACs**.
2. Lines 69-84 represent the authors' contribution and the writing is sloppy and all over the place. So are the authors trying to evaluate how good SoTA methods predict the mean-price on the newly generated orders? Doesn't this just cover the cross-entropy aspect that GenAI literature uses for evaluation? Where's the realism here?
3. It is unclear from lines 86-89 why model derailment is due to true data seeding. Care to discuss?
4. There's missing information about *coletta* and limited results for GOOG (lines 390-394). What missing info?
5. In Figure 6, it is evident that the trend of MO$_0$, and, especially, MO$_1$ aren't captured by *lobs5*. How do you justify this?

Minors:
1. There might be a missing reference in line 76 where you stat "Our aggregator functions are closely inspired by metrics used in literature,
such as spread etc.". How are they inspired by the literature? Which work specifically are you inspired from?
2. Who said that GANs are worst-case aggregators? Why is that?
3. It would be better to introduce already the models you're using in the benchmark in line 86. Why only 2 models if you're proposing a benchmark? There are plenty of other generic time series generation models that you can try to adapt for LOB [1-4].
4. Reference sections/equations correctly:
* e.g., line 265 $\rightarrow$ Equation~\eqref
* e.g., line 307 $\rightarrow$ Section~\ref
5. Lines 97-98 and 98-99 are the same sentence. This is where the authors also reveal their identity.
6. Nobody calls cross-entropy *xent*. Please amend this.

### Questions
See weaknesses, and the following:

1. Have you tried the KL-divergence for $\mathbb{D}$ in Eq. 1? Why is L1 more suitable? Can you run some experiments please to see this effect?
2. Does Figure 2 measure the L1 loss on all these dimensions?
3. Fig 15 $\rightarrow$ So, you trian a GAN on real and generated data from *lobs5* and you achieve an AUCROC of 82\%? This means that the generated orders are easily identified as fake, undermining what the authors claim in their original works. How come? What's the AUCROC for *coletta* and the *baseline*?
4. I might have missed it but what's the *baseline* model here?

### Soundness
2

### Presentation
2

### Contribution
1
