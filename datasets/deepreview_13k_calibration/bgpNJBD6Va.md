# No Preference Left Behind: Group Distributional Preference Optimization

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 6, 6

## Abstract
Preferences within a group of people are not uniform but follow a distribution. While existing alignment methods like Direct Preference Optimization (DPO) attempt to steer models to reflect human preferences, they struggle to capture the distributional pluralistic preferences within a group. These methods often skew toward dominant preferences, overlooking the diversity of opinions, especially when conflicting preferences arise. To address this issue, we propose Group Distribution Preference Optimization (GDPO), a novel framework that aligns language models with the distribution of preferences within a group by incorporating the concept of beliefs that shape individual preferences. GDPO calibrates a language model using statistical estimation of the group's belief distribution and aligns the model with belief-conditioned preferences, offering a more inclusive alignment framework than traditional methods. In experiments using both synthetic controllable opinion generation and real-world movie review datasets, we show that DPO fails to align with the targeted belief distributions, while GDPO consistently reduces this alignment gap during training. Additionally, our evaluation metrics demonstrate that GDPO outperforms existing approaches in aligning with group distributional preferences, marking a significant advance in pluralistic alignment.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investagates the issue that existing LLM alignment methods like DPO tend to favor majority preferences while overlooking minority views, failing to capture the full range of preferences within groups. To solve this issue, the authors propose to incorporate the concept of "beliefs" that shape individual preferences, use statistical estimation to model group belief distributions, and align the model with belief-conditioned preferences. At the inference time, a belief is selected first and then the response is generated conditioned on the selected belief. Experiments with both synthetic data and real-world movie reviews shows some improvement of the proposed GDPO.

### Strengths
It is important to note the minority preference in current LLMs, since the LLMs tend to response with dominant preferences with in majority.

The proposed method is conceptually simple and easy to implement based on the details.

The paper is well-presented and easy to follow.

### Weaknesses
While the motivation to note the minority preference is crucial, the proposed GDPO might not sufficiently fulfill the motivation.

1. The "belief" distribution is predefined, which makes it hard to take into account a wide range of preferences. The method relies on a static, pre-determined set of beliefs, which may not capture the nuanced and diverse spectrum of human opinions. This predefinition limits the model's ability to adapt to novel or unforeseen viewpoints, potentially leading to a biased representation of preferences. The assumption that beliefs can be neatly categorized and quantified might oversimplify the complex nature of human cognition and preference formation. The method does not account for the dynamic and evolving nature of beliefs, which can change over time and in response to new information.

2. At the inference time, a "belief" is selected first. The selected "belief" could also overlook the preference of minority. The inference process, which involves selecting a belief before generating a response, introduces a potential bottleneck. This selection process might inadvertently favor more common beliefs, thereby diminishing the representation of minority preferences. The method does not guarantee that the selected belief will align with the specific minority preference that the model is intended to capture. This approach could lead to a situation where the model still primarily generates responses that reflect majority viewpoints, even if it is capable of generating minority-aligned responses.

3. In the experiment of movie review, the "belief" is implemented with rating scores. However, the rating routain of different persons may be varying. Besides, the rating score can hardly reflect the minority preference. Using rating scores as a proxy for beliefs is a simplification that may not accurately capture the underlying reasons for those ratings. The rating system is subjective and can be influenced by various factors, such as personal biases, mood, and expectations, which are not directly related to the content of the movie. The rating score provides a limited view of the user's complex preferences and cannot fully represent the nuances of their opinions. The approach does not consider the possibility that users may have different interpretations of the rating scale, leading to inconsistencies in the representation of beliefs.

### Questions
1. How the proposed method could solve the issue of overlooking minority preference? Could the authors provide some intuitive explanation?

2. Could the authors provide some cases where the conflicted preference issues is resolved?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel framework called Group Distributional Preference Optimization (GDPO) designed to align language models with the diverse and pluralistic preferences within a group. Unlike existing methods such as DPO, which tend to skew towards dominant preferences and overlook the diversity of opinions, GDPO incorporates the concept of beliefs that shape individual preferences, calibrating models through statistical estimation of the group's belief distribution. Experiments on synthetic controllable opinion generation and real-world movie review datasets demonstrate that GDPO outperforms existing approaches in aligning with group distributional preferences, marking a significant advancement in pluralistic alignment.

### Strengths
1. The paper introduces a novel group-wise perspective in preference optimization, which significantly enhances the effectiveness and practicality of fine-tuning methods compared to existing DPO approaches that often skew towards dominant preferences.

2. The writing is direct and concise, making the paper easy to read and understand. The authors effectively convey complex ideas and methodologies.

3. The experimental design is precise and well-aligned with the core objectives outlined in the introduction. The experiments on both synthetic and real-world datasets clearly demonstrate the paper's contributions, reinforcing the effectiveness of the proposed GDPO framework.

### Weaknesses
- **Belief Set Design**: The need to design specific belief sets for each dataset based on its domain characteristics may limit the scalability and generalizability of the proposed Group Distributional Preference Optimization  framework. This requirement adds an additional layer of complexity and could be a barrier to broader adoption. The process of identifying and defining these belief sets is not clearly articulated, raising concerns about the subjectivity and potential bias introduced during this step. The paper lacks a systematic approach for determining the appropriate number and content of beliefs, which could lead to inconsistent performance across different datasets. Furthermore, the reliance on predefined belief sets may not capture the full spectrum of nuanced opinions present in real-world scenarios, potentially limiting the effectiveness of the method in complex, multifaceted domains. 

- **Training Efficiency**: The training process for GDPO involves calculating the calibration loss $l_{	ext{cal.}}$ for each belief in the set, leading to a significant increase in computational requirements. Specifically, the overall training time could be approximately $ |\mathcal{B}| $ times longer than that of conventional DPO, where $ |\mathcal{B}| $ is the number of beliefs. Addressing this efficiency issue is crucial for the practical implementation of GDPO. The paper does not provide a detailed analysis of the computational overhead associated with the calibration loss, nor does it explore potential optimization strategies to mitigate this issue. This lack of clarity makes it difficult to assess the practical feasibility of the proposed approach, especially when dealing with large-scale datasets or complex models.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies on the preference alignment of LLMs and proposes a conditional distributional preference optimization method with utilizing belief information. However, this work has also some limitations on technique contributions and model applicability. As such, I think this work is bordline and relatively incline to negative.

### Strengths
1. This work studies on an interesting problem.

2. The proposed method is simple and easily implemented.

3. Extensive experiments on bot synthetic and real-world datasets are conducted to validate the effectiveness of the proposed method. 

4. The paper is well-writing.

### Weaknesses
1. The technical contribution appears limited. The proposed method is a simple extension of Distributional Preference Optimization (DPO), and the authors do not provide substantial insights to reveal the intricate properties of the proposed method.

I would suggest the authors conduct more analyses to demonstrate why the proposed strategy is crucial, potentially even a "game-changer" in this field. Theoretical analyses would be particularly beneficial.

2. Another concern pertains to the applicability of the proposed method, given that the belief distribution should be provided.

3. In terms of experiments, I have a suggestion: given that the authors claim their strategy can be integrated with various alignment losses, it would be advantageous to test the model performance with other losses beyond DPO (e.g., PPO, KTO) to demonstrate its merits.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
