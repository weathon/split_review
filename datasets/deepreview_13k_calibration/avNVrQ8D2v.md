# PredFormer: Transformers Are Effective Spatial-Temporal Predictive Learners

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Spatiotemporal predictive learning methods generally fall into two categories: recurrent-based approaches, which face challenges in parallelization and performance, and recurrent-free methods, which employ convolutional neural networks (CNNs) as encoder-decoder architectures. These methods benefit from strong inductive biases but often at the expense of scalability and generalization. 
This paper proposes \textbf{\modelname{}}, a pure transformer-based framework for spatiotemporal predictive learning. 
Motivated by the Vision Transformers (ViT) design, \modelname{} leverages carefully designed Gated Transformer blocks, following a comprehensive analysis of 3D attention mechanisms, including full-, factorized-, and interleaved- spatial-temporal attention. 
With its recurrent-free, transformer-based design, \modelname{} is both simple and efficient, significantly outperforming previous methods by large margins. 
Extensive experiments on synthetic and real-world datasets demonstrate that \modelname{} achieves state-of-the-art performance. 
On Moving MNIST, \modelname{} achieves a 51.3\% reduction in MSE relative to SimVP. 
For TaxiBJ, the model decreases MSE by 33.1\% and boosts FPS from 533 to 2364. 
Additionally, on WeatherBench, it reduces MSE by 11.1\% while enhancing FPS from 196 to 404. 
These performance gains in both accuracy and efficiency demonstrate \modelname{}'s potential for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents PredFormer, a pure transformer-based model for spatiotemporal predictive learning, designed to address challenges in balancing computation costs with predictive accuracy. PredFormer leverages Gated Transformer Blocks (GTBs) and a comprehensive exploration of attention mechanisms to surpass previous recurrent-based and convolutional encoder-decoder methods.

### Strengths
- It boasts significant improvements in benchmark tasks involving datasets like Moving MNIST, TaxiBJ, and WeatherBench, showcasing both high accuracy and efficiency.
- The figures in the paper are clean and aesthetically pleasing, which enhances readability.

### Weaknesses
 - Emphasizing "the first pure transformer model in xxx domain" as a main contribution feels minor, given that ViT was introduced in ICLR 2021. Highlighting this three years later may not meet ICLR's innovation standards.
  - Noting that SwinLSTM[1] and OpenSTL[2] have already shown the capability of Transformer in this domain, which will further reduce the novelty of this work.
  - Especially the OpenSTL, which already incorporates and evaluates commonly used transformer or CNN blocks, i.e., ViT, Swin Transformer, Uniformer, MLP-Mixer, ConvMixer, Poolformer, ConvNeXt, VAN, HorNet, and MogaNet.

- The study of spatiotemporal block combinations has already been extensively explored in `various domains` by `numerous Transformer-based works`, such as **Latte** [3]. Therefore, the contribution in this aspect may appear somewhat weak or incremental. 
  - Due to the long sequence length problem of the Spatial-Temporal modeling task, most work delved into the architecture design of spatial block and temporal block, i.e., Latte also proposes 4 different spatial-temporal block variants, which are similar to this paper.

- The regularization and position encoding techniques used in this paper are well discovered in many language and vision papers. Utilizing them directly provides limited contribution.


[1] SwinLSTM: Improving Spatiotemporal Prediction Accuracy using Swin Transformer and LSTM

[2] OpenSTL: A Comprehensive Benchmark of Spatio-Temporal Predictive Learning

[3] Latte: Latent diffusion transformer for video generation

### Questions
Please refer to the weakness part. I will raise my scores if the authors can resolve my concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes PredFormer, a transformer-based model for spatiotemporal predictive learning that replaces conventional recurrent and convolutional architectures with gated transformer blocks. PredFormer employs several encoder configurations—full attention, factorized, and interleaved models—to capture complex spatial and temporal relationships. The model reportedly achieves state-of-the-art results in accuracy and efficiency on multiple datasets, including Moving MNIST, WeatherBench, and TaxiBJ.

### Strengths
1.	The paper is well-written and easy to follow.
2.	The model is evaluated on multiple synthetic and real-world datasets, which highlights its adaptability across different spatiotemporal tasks.
3.	PredFormer demonstrates a reduction in parameters and improved inference speed on specific configurations compared to previous methods, making it potentially applicable for real-time tasks.

### Weaknesses
1.	The model’s design is primarily an adaptation of established concepts from Vision Transformers (ViTs) and gated transformers, without substantial innovation in model architecture or theoretical insight. This limits the paper’s contribution beyond incremental improvements.

2.	The authors should select a single architecture to compare against prior state-of-the-art methods for a fair assessment, as previous works typically present only one variation. Comparisons of different PredFormer architectures should instead be placed in the ablation study section.

3.	The best results for both recurrent-based and recurrent-free methods should be highlighted in bold. Some results from prior methods appear to outperform PredFormer, and this should be clearly indicated.

4.	I noticed that STCF [1] shows superior performance on the TaxiBJ dataset. Why was it not considered in the comparisons?

### Questions
Hope the author can answer the questions in the weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces PredFormer, a novel framework for spatiotemporal predictive learning that is based purely on transformers. Unlike traditional recurrent-based approaches that struggle with parallelization and performance, and recurrent-free methods like CNNs that can lack in scalability and generalization, PredFormer utilizes Gated Transformer blocks inspired by the design of Vision Transformers (ViT). The architecture is informed by a thorough examination of various 3D attention mechanisms—full, factorized, and interleaved spatial-temporal attention—which allows PredFormer to efficiently handle complex spatiotemporal data.

Key contributions of this work include:
- **Innovative Architecture**: A pure transformer-based model that is both simple and highly efficient.
- **Superior Performance**: Significant improvements over existing methods in terms of accuracy and efficiency, as evidenced by substantial reductions in Mean Squared Error (MSE) and increases in Frames Per Second (FPS) across multiple datasets.
- **Versatility Across Datasets**: Demonstrates state-of-the-art performance on diverse datasets, including synthetic (Moving MNIST) and real-world (TaxiBJ, WeatherBench) scenarios.
- **Public Availability**: Plans to release the source code and trained models to facilitate further research and practical applications.

These advancements highlight PredFormer's potential for broad application in areas requiring accurate and efficient spatiotemporal predictions.

### Strengths
The strength of this paper lies in its novel introduction of PredFormer, a pure transformer-based model for spatiotemporal predictive learning. PredFormer innovatively integrates Gated Linear Units (GLUs) with self-attention mechanisms, effectively capturing complex spatiotemporal dynamics. The paper conducts a comprehensive analysis of different 3D attention mechanisms, leading to nine optimized configurations that address varying spatial and temporal resolutions. Extensive experiments on benchmark datasets (Moving MNIST, TaxiBJ, WeatherBench) demonstrate state-of-the-art performance, with significant improvements in accuracy and efficiency. Notably, PredFormer achieves a 51.3% reduction in MSE on Moving MNIST, a 33.1% reduction in MSE on TaxiBJ, and an 11.1% reduction in MSE on WeatherBench, while also offering faster inference speeds. The model's efficiency, broad applicability, and planned public availability of source code and trained models further enhance its impact and potential for real-world applications.

### Weaknesses
 - Firstly, PredFormer has not been evaluated on more complex and challenging datasets, such as Traffic4Cast for traffic flow prediction and Human3.6M for human motion forecasting. This limitation restricts the breadth of the model's validation and leaves questions about its performance on more intricate real-world scenarios.

- Secondly, the experiments primarily use relatively small frame sizes, which makes it difficult to assess the model's effectiveness and scalability when applied to high-resolution data. These limitations suggest that further research is needed to fully demonstrate PredFormer's capabilities in handling complex and high-resolution spatiotemporal data.

- Additionally, the paper does not compare PredFormer with state-of-the-art transformer-based predictive learning methods, such as Earthformer. This omission limits the comprehensiveness of the performance evaluation and makes it harder to establish PredFormer's relative advantages and disadvantages in the context of the latest research.

- As shown in Table 2 and Table 3, PredFormer does not demonstrate a significant advantage in running efficiency compared to recurrent-free methods, and its performance in terms of MSE is similar to these methods. This suggests that while PredFormer offers a novel and theoretically sound approach, its practical benefits in terms of efficiency and performance are not as pronounced as claimed.

### Questions
- Why were more complex and challenging datasets, such as Traffic4Cast for traffic flow prediction and Human3.6M for human motion forecasting, not included in the evaluation? Could you provide insights into how PredFormer might perform on these datasets?

- The experiments primarily use relatively small frame sizes. I suggest that the paper should evaluate PredFormer's effectiveness and scalability when applied to high-resolution data.

- The paper does not compare PredFormer with state-of-the-art transformer-based predictive learning methods, such as Earthformer. Could you provide a comparison with these methods to better understand PredFormer's relative advantages and disadvantages?

- As shown in Table 2 and Table 3, PredFormer does not demonstrate a significant advantage in running efficiency compared to recurrent-free methods, and its performance in terms of MSE is similar. Could you explain why PredFormer does not show a more pronounced improvement in efficiency and performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper present a pure transformer-based architecture for spatiotemporal predictive learning. The authors conduct a detailed exploration of various design choices and training techniques. Their model demonstrates significant performance improvements over established baselines.

### Strengths
- The manuscript is well-organized and clearly written.
- The paper offers a comprehensive analysis of architectural design choices and establishes strong baselines in the field of spatiotemporal predictive learning.
- Extensive experiments, including ablation studies, are performed, which highlight the advantages of the proposed PredFormer model.

### Weaknesses
The technical novelty of the paper appears limited. For instance, the SwiGLU activation function, a core component of the model, is not new and has been explored extensively in other contexts. Additionally, factorized spatial-temporal attention is a well-known approach in video prediction, limiting the originality of the contribution. The paper lacks a rigorous justification for the specific choices of architectural components and their arrangement, making the design seem more like an empirical exploration rather than a principled approach. The performance gains, while present, do not appear to stem from fundamentally new insights but rather from a combination of existing techniques.

### Questions
- Are there any quantitative results regarding the efficiency of the proposed model compared to state-of-the-art recurrent-based methods (e.g., models incorporating Mamba-based architectures)?
- Could video generation models like Diffusion, GANs, or MagViT be adapted for spatiotemporal predictive tasks? How does PredFormer compare to these models in terms of performance and efficiency advantages?

### Soundness
3

### Presentation
4

### Contribution
3
