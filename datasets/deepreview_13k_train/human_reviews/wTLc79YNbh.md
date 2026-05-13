# TimeKAN: KAN-based Frequency Decomposition Learning Architecture for Long-term Time Series Forecasting

- Decision: Accept
- Scores: 3, 5, 8, 8

## Abstract
Real-world time series often have multiple frequency components that are intertwined with each other, making accurate time series forecasting challenging. Decomposing the mixed frequency components into multiple single frequency components is a natural choice. However, the information density of patterns varies across different frequencies, and employing a uniform modeling approach for different frequency components can lead to inaccurate characterization. To address this challenges, inspired by the flexibility of the recent Kolmogorov-Arnold Network (KAN), we propose a KAN-based Frequency Decomposition Learning architecture (TimeKAN) to address the complex forecasting challenges caused by multiple frequency mixtures. Specifically, TimeKAN mainly consists of three components: Cascaded Frequency Decomposition (CFD) blocks, Multi-order KAN Representation Learning (M-KAN) blocks and Frequency Mixing blocks. CFD blocks adopt a bottom-up cascading approach to obtain series representations for each frequency band. Benefiting from the high flexibility of KAN, we design a novel M-KAN block to learn and represent specific temporal patterns within each frequency band. Finally, Frequency Mixing blocks is used to recombine the frequency bands into the original format. Extensive experimental results across multiple real-world time series datasets demonstrate that TimeKAN achieves state-of-the-art performance as an extremely lightweight architecture.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents TimeKAN, a Kolmogorov-Arnold Network (KAN)-based model for long-term time series forecasting, designed to handle complex multi-frequency patterns in real-world data. Traditional models struggle with mixed frequencies, but TimeKAN addresses this with a three-part architecture: Cascaded Frequency Decomposition to separate frequency bands, Multi-order KAN Representation Learning to model each band’s specific patterns using adaptable polynomial orders, and Frequency Mixing to recombine frequencies effectively. Experiments show that TimeKAN achieves superior accuracy and efficiency compared to existing models, making it a robust, lightweight solution for complex TSF tasks.

### Strengths
**Exploratory Application of KAN to Time Series Forecasting**: The paper attempts to introduce Kolmogorov-Arnold Networks (KAN) into time series forecasting, using multi-order polynomial representations to handle the complexities of different frequency components. While KAN has not been widely applied in this area, this effort demonstrates its potential flexibility in data fitting and offers an alternative approach to traditional MLPs.

 **Comprehensive Experimental Design**: The paper includes experiments across various time series datasets, such as weather, electricity, and energy data, covering diverse scenarios. Additionally, it conducts ablation studies to examine the effects of each module. These experiments help to assess TimeKAN’s performance and may provide a reference point for further research.

### Weaknesses
 **Lack of Innovation**: The primary contribution of this paper is the integration of the Kolmogorov-Arnold Network (KAN) into time series forecasting, yet the work does not introduce novel methods or substantial breakthroughs in methodology. While the inclusion of KAN is somewhat new, other components, such as frequency decomposition and mixing, are mature techniques, and the paper does not propose innovative applications or enhancements to these. Specifically, the frequency decomposition relies on standard Fourier transforms, and the mixing process uses simple concatenation or addition, lacking any sophisticated adaptive mechanisms. Overall, this work appears more like a combination of existing technologies rather than a genuinely innovative study.

**Absence of Comparison with Cutting-Edge Models**: The experiments lack direct comparisons with state-of-the-art models, especially those in high demand for time series forecasting, such as large language models (LLMs) and foundation models. Given current research trends, these models have become widely adopted benchmarks. Without such comparisons, the effectiveness of the proposed method remains unclear, especially as the improvements presented are relatively limited compared to advancements in mainstream approaches. For instance, the paper does not benchmark against models like the Transformer-based methods or recent state-space models, which have demonstrated strong performance in long-term time series forecasting. This omission makes it difficult to assess the practical value of TimeKAN.

 **Reliance on KAN, a Model with Limited Validation**: The foundation of TimeKAN is the KAN model, which has not yet been widely validated or accepted. Its theoretical correctness and practical effectiveness remain uncertain, which casts doubt on the reliability and generalizability of TimeKAN as a whole. If there are inherent issues with KAN, such as instability in training or sensitivity to hyperparameter tuning, the predictive performance and stability of TimeKAN could be compromised, making the paper's conclusions less convincing. The paper does not address these potential issues or provide any robustness analysis of the KAN component.

**Insufficient Analysis of Computational Efficiency**: While the paper claims that TimeKAN is more lightweight than existing methods, it lacks an in-depth analysis of its actual computational efficiency, especially compared to more mainstream and optimized time series models. Additionally, there is no quantification of the computational cost associated with KAN’s multi-order polynomial calculations when handling long-sequence data. Given that many time series tasks require efficient real-time computations, focusing solely on parameter reduction does not adequately demonstrate TimeKAN’s advantage in computational efficiency; the absence of data on inference speed and computational cost undermines its practical applicability. The paper should include a detailed breakdown of the computational cost of each module, including the FFT, KAN layers, and mixing operations, to provide a comprehensive view of its efficiency.


**Focus on Single-Task Performance Rather Than Generalized Representation**: A dominant trend in time series modeling now follows the approach of large language models (LLMs) to develop foundation models and leverage self-supervised representation learning. This approach enables generalization across various tasks and domains, ultimately aiming for a “one-fit-all” solution. However, this paper remains focused on improving single-task performance in time series forecasting (TSF), which may be of limited value in light of the broader goals of the field. Furthermore, the improvements reported in the experimental results are relatively modest, and without statistical significance testing, it remains unclear if these gains are truly meaningful or could simply be attributed to random variation.

### Questions
**To my knowledge, KAN itself has not been formally accepted, meaning it has not undergone rigorous peer-reviewed validation. If KAN’s theoretical foundation is later found to be flawed, would this impact the validity of this paper?** – If the underlying theory or structure of KAN is later shown to have limitations or inaccuracies, would the overall reliability of TimeKAN be compromised? Has the author considered this risk, and are there alternative solutions in place?

**In the experimental section, this paper does not compare TimeKAN with current state-of-the-art models (such as large language models or foundation models), making it difficult to assess its actual performance** – Without direct comparisons with these advanced models, can TimeKAN demonstrate a significant advantage? If the authors believe TimeKAN holds particular value in computational efficiency or predictive accuracy, could more data be provided to quantify this advantage?

**A major trend in time series research is developing foundation models, inspired by large language models, to generalize across domains and tasks. However, it is unclear if TimeKAN’s current design can support such robust representation learning** – Can TimeKAN truly compete with established frameworks like Transformers in terms of generalization and adaptability? If not, have the authors considered alternative approaches to enhance TimeKAN’s structural robustness and flexibility for broader applications?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors propose a time series forecasting method based on KAN. TimeKAN uses frequency decomposition and KAN to effectively capture temporal correlations of the data. Experiments show the effectiveness of TimeKAN based on real-world datasets.

### Strengths
1. A vivid introduction and related work section to explain the background of time series forecasting and KAN.
2. A clear figure to illustrate the overall framework of TimeKAN. In the methodology section, all components are detailed. 
3. Good ablation study to test the effectiveness of the different components of the model.

### Weaknesses
1. The author does not explain why TimeKAN does not perform well in the Electricity dataset. It would be helpful if the authors could provide potential reasons or hypotheses for why TimeKAN underperforms on the Electricity dataset specifically. It's crucial to understand if this is a limitation of the model or a data-specific issue. For instance, is the frequency content of the Electricity dataset fundamentally different, or is there a mismatch between the model's assumptions and the data characteristics?
2. From Table 4, I do not see a huge increase with KAN compared to MLP models. Generally, if these results are similar, mostly, KAN is much slower than MLP. It would be good to see runtime comparisons between KAN and NLP implementations. Additionally, if KAN is slower than MLP in practice, it would be beneficial for authors to discuss more reasons why we prefer KAN over MLP. The paper should quantify the computational overhead of KAN compared to MLP, and justify the use of KAN if the performance gains are marginal, especially considering the potential increase in training time and resource consumption.
3. For the look-back window, the authors do not compare TimeKAN with other models. For most models, when the prediction length is fixed, the prediction accuracy will increase as the look-back window increases. It is beneficial to provide a comparative analysis of TimeKAN's performance with varying look-back windows compared to other baseline models. This would provide a more comprehensive evaluation of TimeKAN's capabilities relative to existing methods. The analysis should include a discussion of how the model's performance scales with increasing look-back window sizes, and whether there are diminishing returns or potential overfitting issues.
4. For baseline methods, it is better to choose more frequency-based (such as FreTS) methods since frequency decomposition is a key contribution. The current baseline methods do not fully address the frequency decomposition aspect of the proposed method. Including frequency-based baselines would provide a more direct comparison and highlight the specific advantages of the proposed approach.

### Questions
1. See weaknesses.
2. Could you provide a short theoretical analysis about why in some cases in time series forecasting, KAN is better than MLP?
3. For Table 2, why not include the electricity dataset?
4. For KAN, you mentioned that the Kolmogorov-Arnold representation theorem states that any multivariate continuous function can be expressed as a combination of univariate functions and addition operations. Could you explain more about how it can capture multivariate correlations?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
TimeKAN is a time series forecasting model that combines frequency decomposition, representation learning, and mixing. It first uses a moving average to separate high and low frequencies, creating multi-level sequences that are embedded into a high-dimensional space. Cascaded Frequency Decomposition (CFD) blocks progressively isolate each frequency band. The Multi-order KAN Representation Learning (M-KAN) blocks use Kolmogorov-Arnold Networks to capture temporal patterns within each frequency band independently. Finally, the Frequency Mixing blocks recombine these decomposed bands to restore the original sequence, which is then used for forecasting through a linear layer

### Strengths
1	Clarity and Structure: The paper follows a logical flow from problem statement to conclusions, making complex ideas accessible.
	2.	Thorough Background: A strong review of related work provides valuable context, situating the contribution within the field.
	3.	Detailed Experiments: Comprehensive experiments across multiple datasets support the model’s performance claims, with ablation studies highlighting component effectiveness.
	4.	Focused Writing: The paper stays on topic, avoiding unnecessary details and maintaining focus on the core contribution

### Weaknesses
Depth in Explanation: The methodology section could offer more detail on complex components like Kolmogorov-Arnold Networks for greater accessibility.



### Questions
What if we split the frequency band to more layers (more than 3 for example ). Will it increase performance ?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper explores a method for decomposing mixed frequency components into distinct single-frequency components to improve time series forecasting accuracy. The proposed approach, called TimeKAN, is based on the Kolmogorov-Arnold Network (KAN). TimeKAN's process consists of three key components: (1) Cascaded Frequency Decomposition (CFD) blocks, which use a bottom-up cascading approach to obtain series representations for each frequency band; (2) Multi-order KAN Representation Learning (M-KAN) blocks, which capture and represent specific temporal patterns within each frequency band; and (3) Frequency Mixing blocks, which recombine the separated frequency bands back into the original series format.

The study demonstrates that TimeKAN outperforms several state-of-the-art forecasting methods, including Autoformer, FEDformer, and iTransformer, by achieving lower MSE and MAE across multiple time series datasets such as Weather, ETTh2, and ETTm2.

### Strengths
1. Figure 1 is beautifully designed and provides an intuitive overview of each component in the new TimeKAN method, as well as how they connect.

2. The study makes effective use of large-scale datasets and performs comparisons with a variety of other methods (including CNN-based and Transformer-based models), demonstrating the advantages of TimeKAN. The model is also tested across different prediction lengths, and for datasets where performance is less optimal, the paper offers thorough explanations and detailed insights.

3. The analysis delves into several key components of TimeKAN, such as Upsampling, Depthwise Convolution, and Multi-order KANs. I especially appreciated this section, as it not only establishes that TimeKAN outperforms other deep learning methods but also shows that each individual component of TimeKAN is optimally designed.

### Weaknesses
1. Section 3.2 appears somewhat disorganized. While the overall logic is clear, the expression could be refined for clarity. Additionally, more mathematical details and background should be provided, which can be included in the appendix.

2. If possible, please add more data to Table 5 in Section 4.3. Supplement it with the performance of other methods in Table 1 on parameters (params) and MAC across these six datasets.

### Questions
N/A

### Soundness
3

### Presentation
4

### Contribution
4
