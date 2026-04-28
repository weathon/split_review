# AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Graphical User Interface (GUI) agents hold great potential for automating complex tasks across diverse digital environments, from web applications to desktop software. However, the development of such agents is hindered by the lack of high-quality, multi-step trajectory data required for effective training. Existing approaches rely on expensive and labor-intensive human annotation, making them unsustainable at scale. To address this challenge, we propose \ourwork, a scalable data synthesis pipeline that generates high-quality GUI agent trajectories by leveraging web tutorials. Our method automatically gathers tutorial-like texts from the internet, transforms them into task goals with step-by-step instructions, and employs a visual-language model (VLM) agent to simulate their execution in a real digital environment. A VLM-based evaluator ensures the correctness of the generated trajectories. We demonstrate that training GUI agents with these synthesized trajectories significantly improves their grounding and planning performance over the current models. Moreover, our approach is more cost-efficient compared to traditional human annotation methods. This work underscores the potential of guided replay with web tutorials as a viable strategy for large-scale GUI agent training, paving the way for more capable and autonomous digital agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
1. The paper introduces AgentTrek, a scalable data synthesis pipeline that generates high-quality GUI agent trajectories
by leveraging web tutorials.
2.  The method collects web tutorials from the internet, transforms them into structured task goals with step-by-step instructions, and uses a visual-language model (VLM) agent to simulate their execution in a digital environment. ​ A VLM-based evaluator ensures the correctness of the generated trajectories.
3. The paper provides experimental results and analayis showing that agents trained with the synthesized data outperform those trained on existing datasets in both grounding and planning capabilities.
4. The authors emphasize that the method is more cost-efficient than traditional human annotation methods, making it a practical solution for large-scale GUI agent training

### Strengths
1. It is a novel pipeline that leverages web tutorials to synthesize high-quality GUI agent trajectory data at scale. This is a valuable contribution to the field, addressing the scarcity of reliable and scalable trajectory data. The proposed pipeline significantly reduces the cost of data collection compared to traditional human annotation
2. The paper is well-structured and clearly explains the steps involved in the data filtering
3. The dataset is comprehensive, containing a wide range of task types, platforms, and web environments.

### Weaknesses
1. The paper does not provide a baseline to compare how using trajectory data compares with just using textual data. It would be beneficial to see how much the different elements( DOM/HTML structures, AXTree data, intermediate reasoning steps, full video recordings, and corresponding screenshots for each action) contribute to the dataset effectiveness.
2. The paper deals with only web-based tutorials and shows evaluation on only 2 benchmarks. It would be beneficial to expand the evaluation by including additional benchmarks such as MiniWob.
3. The paper lacks an analysis of potential failure cases. For example, is the trajectory data still as effective when the number of steps increase.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces AgentTrek, a data synthesis pipeline that generates web agent trajectories from online tutorials. It automatically collects tutorials, converts them into task sequences, and uses VLMs to simulate and evaluate these tasks. Results show that agents trained with AgentTrek data perform better in task grounding and planning than those using traditional datasets, providing a cost-effective solution for large-scale web agent training.

### Strengths
A clear pipeline for generating complex agent trajectories from web tutorials.

### Weaknesses
1. In the Mind2Web experiment, it is clear that there is overlap between the training data and those in Mind2Web-test, with likely overlap in tasks, websites as well as domains. This overlap should be clarified, as it undermines the intended out-of-domain evaluation of Mind2Web.
2. The total number of trajectories remains limited, staying within the same scale as Mind2Web (in thousands). And the effectiveness is not good enough compared to the training data of Mind2Web (when the data size is 4x).
3. The comparison on grounding is not very meaningful, as performance significantly lags behind recent work focused specifically on grounding. (And empirically, a significant gain is from changing the backbone to Qwen 2 VL, compared to SeeClick and CogAgent.)
4. The web results on ScreenSpot, especially for icons, are not strong, which raises further questions about possible overfitting to specific websites or tasks in Mind2Web.
5. Some writing issues:  
   - baseline results should clearly indicate their sources
   - duplicate entries in the reference
   - wrong reference
   - more details of the evaluation on Mind2Web should be provided. (This is not minor. As there are huge differences with respect to the settings in table 6)
   - the synthesized data is essentially web agent trajectories. No need to always overclaim it to GUI agent trajectory. It only confuses people.

### Questions
1. The overlap issue to Mind2Web.
2. Is there any other way to support the effectiveness of the synthesized data?
3. If possible, show the effectiveness of the synthetic data when it is further scaled up.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The AgentTrek framework introduces a scalable pipeline for generating high-quality GUI agent trajectory data by utilizing web tutorials. It automates the collection of tutorial-like instructions from the internet, transforms them into structured tasks, and uses a visual-language model agent to simulate and execute these tasks in real digital environments. An evaluator model verifies the generated trajectories to ensure accuracy, reducing reliance on labor-intensive human annotations. Experimental results show that models trained with AgentTrek-generated data outperform those trained on existing datasets, especially in task planning and GUI grounding. This framework offers a cost-effective, automated solution for training GUI agents on a large scale.

### Strengths
The AgentTrek framework leverages online tutorials to automatically generate high-quality GUI agent trajectory data, automating the data generation process and reducing the need for manual data collection. Through an evaluator model, it verifies the generated trajectories, with a multi-layered generation and evaluation mechanism to ensure data quality and effectiveness.

Agents trained on AgentTrek-generated data perform exceptionally well in several benchmark tests (such as ScreenSpot and Multimodal-Mind2Web), especially in task planning and GUI element recognition, significantly outperforming traditional datasets.

### Weaknesses
Certain technical details, such as automatic labeling and tutorial filtering, are only briefly mentioned in the paper, lacking more comprehensive explanations.

The paper notes that the success rate of generating effective trajectories is only 39.1%, based on GPT-4o Mini. Although GPT-4o Mini is relatively cost-effective, achieving larger-scale data generation with the current success rate remains challenging. There should be some indications if experiments are conducted with alternative open-source models to assess the feasibility and effectiveness of data construction within this framework.

Another consideration is the broader generalization of the framework for more complex computer control tasks. Many tasks may lack corresponding web tutorials or have very limited resources, especially those requiring highly precise and complex control, which will also lead to the data/categories bais issue. Do you have any thoughts or attemptions on these situations?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
