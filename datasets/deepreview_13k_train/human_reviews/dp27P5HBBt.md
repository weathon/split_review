# Periodicity Decoupling Framework for Long-term Series Forecasting

- Decision: Accept
- Scores: 8, 8, 3, 8

## Abstract
Convolutional neural network (CNN)-based and Transformer-based methods have recently made significant strides in time series forecasting, which excel at modeling local temporal variations or capturing long-term dependencies. However, real-world time series usually contain intricate temporal patterns, thus making it challenging for existing methods that mainly focus on temporal variations modeling from the 1D time series directly. Based on the intrinsic periodicity of time series, we propose a novel Periodicity Decoupling Framework (PDF) to capture 2D temporal variations of decoupled series for long-term series forecasting. Our PDF mainly consists of three components: multi-periodic decoupling block (MDB), dual variations modeling block (DVMB), and variations aggregation block (VAB). Unlike the previous methods that model 1D temporal variations, our PDF mainly models 2D temporal variations, decoupled from 1D time series by MDB. After that, DVMB attempts to further capture short-term and long-term variations, followed by VAB to make final predictions. Extensive experimental results across seven real-world long-term time series datasets demonstrate the superiority of our method over other state-of-the-art methods, in terms of both forecasting performance and computational efficiency. Code is available at https://github.com/Hank0626/PDF.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper decouples variations of different scales in multi-variate long-term time series based on their periodicity. It then leverages the respective modeling strengths of CNNs and Transformer models to represent these scale-distinct variations. Extensive experiments on multiple long-term time series forecasting datasets demonstrate that the proposed Periodic Decoupling Framework (PDF) method outperforms the latest state-of-the-art approaches across various forecasting time intervals.

### Strengths
Strengths:
1) The proposed periodicity decoupling framework is a novel and efficient solution to capture 2D temporal variation modeling for long-term series forecasting. Besides, modeling long-term and short-term variations also offers a new perspective for time series forecasting. 
2) The fusion of CNNs and Transformers is prevalent in CV and NLP. This paper bridges time series studies with other advanced domains, introducing the PDF framework by leveraging the strengths of both architectures. The PDF demonstrates outstanding performance and efficiency in time series tasks, as evidenced by thorough experiments.
3) The authors analyze the computational burden with other state-of-the-art methods and demonstrate the efficiency of the proposed method.
4) The overall paper is well-organized and easy to follow.

### Weaknesses
1) The channel-independent strategy focuses on the dependencies of the time dimension adopted in this work and is inspired by PatchTST [1]. However, channel dependency is also helpful. In other works, such as Crossformer [2], modeling channels have also been beneficial to some extent in forecasting results. A more robust justification for this choice is needed. Specifically, while the authors mention that channel-independent strategies can mitigate data drift, they do not provide a clear explanation of how this occurs within their framework. Furthermore, they do not discuss the potential loss of information that could result from ignoring inter-channel dependencies, especially in datasets where these relationships are strong.
2) The innovativeness of the patching method in this work needs to be articulated more specifically. What distinguishes this patching approach from other recent patch-based works (such as PatchTST [1] and PETformer [3])? The current description lacks a detailed explanation of how the proposed patching method differs from existing techniques in terms of patch construction and information preservation. It is not clear how the proposed method ensures that long-term dependencies are captured more effectively than in other patch-based approaches. A more in-depth analysis of the specific advantages of this patching strategy is needed.

### Questions
1) What are the benefits of long-term variation and short-term variation extractors?
2) The periodicity obtained is adaptive to the time series of input?
3) It is reasonable to model 2D temporal short-term and long-term variations. Is it possible to model 3D variations in time series?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Real-world time series forecasting is challenging, since it usually contains intricate temporal patterns. This paper focuses on exploits intricate temporal patterns by decoupling the complex series into simpler series to achieve long-term series forecasting. Thus, the authors developed  a novel Periodicity Decoupling Framework (PDF) for long-term series forecasting by capturing 2D temporal variation modeling. Extensive experimental results across  seven real-world long-term time series datasets demonstrate the superiority of the proposed method over other state-of-the-art methods, in terms of both forecasting performance and computational efficiency.

### Strengths
- It is reasonable and interesting to decouple the complex 1D time series into simpler series with various variations based on periodicity.
- The proposed multi-periodic decoupling block is a novel and effective solution to capture various periods of the input series. Based on the periodicity of the time series, the 1D time series are decoupled into simpler short- and long-term series.
- Extensive experiments demonstrate the effectiveness of the proposed over other state-of-the-art methods (e.g., TimesNet, TiDE) across various long-term time series datasets.
- The overall paper is well-written and easy to follow.

### Weaknesses
 - How to decouple the time series remains an open question. Although the authors propose a simple yet effective periodicity-based strategy to decouple the time series, how to evaluate the effectiveness of decouple strategy has been less explained. Specifically, the paper lacks a clear metric or ablation study to demonstrate that the chosen decoupling method is superior to other possible approaches, such as using different frequency bands or employing more sophisticated decomposition techniques. The current justification relies solely on the final forecasting performance, which could be influenced by other factors.
- Experiments show the computational efficiency of the proposed methods over other transformer-based methods. However, the authors have not compared the running time of different methods. While Multiply-Accumulate Operations (MACs) provide a theoretical measure of computational cost, they do not directly translate to real-world running time, which can be affected by hardware, software, and implementation details. A direct comparison of running times would provide a more practical evaluation of the method's efficiency.

### Questions
- Is there other ways to decouple time series? Besides, how to evaluate the effectiveness of the proposed decoupled strategy?
- It is recommended to compare the running time of other methods.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel approach called the Periodicity Decoupling Framework (PDF) for enhancing time series forecasting. The PDF method comprises three main components: the multi-periodic decoupling block (MDB) to extract 2D temporal variations from 1D time series, the dual variations modeling block (DVMB) for capturing short-term and long-term variations, and the variations aggregation block (VAB) for making predictions. Extensive experiments on seven real-world long-term time series datasets demonstrate the effectiveness of proposed methods.

### Strengths
1. this paper is easy to follow.
2. this paper studies a classic problem, time series forecasting.

### Weaknesses
1. the motivation. This paper is not well-motivated. Why do we need 2D states to capture periodicity in time series forecasting? Do the authors show the necessity of the 2D modeling for periods?
2. the novelty is limited. The biggest contribution of this paper, the formulation of 1D to 2D transformation seems to be the same as TimesNet [1], which makes the novelty largely limited.
3. the contribution is a little weak. Compared with existing works (such as TimesNet), it only revises several blocks for time series forecasting. The methods don't contribute well to the community.
4. missing of related work. More periodic modeling works should be discussed [2,3]. Also, differences compared with TimesNet should be discussed.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a Periodicity Decoupling Framework (PDF) to address the challenges of long-term time series forecasting, which traditionally have intricated temporal patterns. The proposed PDF decouples the time series into distinct short-term and long-term series based on its periodicity. Following this, the dual variations modeling block (DVMB) is employed to extract both short-term and long-term variations. Finally, the variations aggregation block (VAB) aggregates the extracted variations for final predictions. Experimental results show that PDF achieves state-of-the-art performance while maintaining low computational cost.

### Strengths
1) Decoupling long-term and short-term variations from complex time series based on periodicity seems reasonable. Besides. the proposed method captures long-term and short-term variations, which fully utilizes the ability of Transformer to model global variations and CNNs to model local variations. 
2) The paper proposes a simple yet effective way to extract the dual variations of short-term and long-term variations. Besides, the foundational design is well-motivated and robustly substantiated.
3) The significance of both short-term and long-term variations in time series forecasting is adeptly highlighted. The manuscript is well-written and understandable, and the figures and formulas are well-presented.

### Weaknesses
1)Unlike the frequency selection strategy in TimesNet [1], the reason for using a different strategy in the Multi-periodic Decoupling Block needs to be further explained. Specifically, the paper should elaborate on why selecting frequencies based on both amplitude and value is superior to solely relying on the top-k amplitudes as done in TimesNet. The potential drawbacks of this approach, such as the risk of including less representative frequencies, should also be discussed.
2)Were the experimental data in the article averaged over multiple runs with different random seeds? This is crucial for ensuring the robustness and reliability of the experimental results. The absence of such averaging could lead to conclusions based on potentially biased outcomes.
3)The experimental section mentions that the significant performance gain of TiDE [2] in traffic largely stems from static covariates. It would be preferable to provide experiments to substantiate this claim by ablating the static covariates in the TiDE model and showing the performance difference on the traffic dataset.

### Questions
1) What is the effects of different perodics?  Since the proposed method lies in periodic to decouple the original time series.  
2) Can the proposed method applied to other time series applications, like time series classification?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
