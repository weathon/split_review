# MobileAIBench: Benchmarking LLMs and LMMs for On-Device Use Cases

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
The deployment of Large Language Models (LLMs) and Large Multimodal Models (LMMs) on mobile devices has gained significant attention due to the benefits of enhanced privacy, stability, and personalization. However, the hardware constraints of mobile devices necessitate the use of models with fewer parameters and model compression techniques like quantization. Currently, there is limited understanding of quantization's impact on various task performances, including LLM tasks, LMM tasks, and, critically, trust and safety. There is a lack of adequate tools for systematically testing these models on mobile devices. To address these gaps, we introduce MobileAIBench, a comprehensive benchmarking framework for evaluating mobile-optimized LLMs and LMMs. MobileAIBench assesses models across different sizes, quantization levels, and tasks, measuring latency and resource consumption on real devices. Our two-part open-source framework includes a library for running evaluations on desktops and an iOS app for on-device latency and hardware utilization measurements. Our thorough analysis aims to accelerate mobile AI research and deployment by providing insights into the performance and feasibility of deploying LLMs and LMMs on mobile platforms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a benchmarking infrastructure for measuring on-device LLMs and LMMs in mobile deployments. The system report a wide set of evaluation metrics, including quality benchmarks for standard NLP tasks, multimodal tasks, and trust/safety. The authors evaluated a series of open models on an iPhone 14 device and provided insights on the deployability of those models on mobile platforms.

### Strengths
- Exciting new topic. Running LLMs (and possibly LMMs) on-device is important for enhanced privacy, and, under certain conditions, it provides enhanced performance and UX.
- I appreciate the extensive evaluation metrics, on top of the standard performance utilization: trust and safety, but also the qualitative metrics under a wide range of NLP/LMM tasks.
- Good quality of writing, figures etc. I do have a few suggestions for further improvements, mentioned next.

### Weaknesses
 - Missing important related works:
  * MELTing point: Mobile Evaluation of Language Transformers, from Laskaridis et al.
  * Small Language Models: Survey, Measurements, and Insights, from Zhenyan Lu et al.
- Authors are claiming that this is the first work "to provide a thorough benchmarking and analysis of open source LLMs". I suggest they reduce such strong claims.
- I would expect from a paper like this to list (if not include in the evaluation) the available on-device frameworks instead of sticking to llamacpp. For instance: MLC LLM, MediaPipe from Google, PyTorch ExecuTorch, Apple MLX should be mentioned.
- Details about the followed methodology are missing. How did the authors run the evaluation tasks on-device? Did they automate the process? Did they repeat the process multiple times? Did they reboot the device per task? Did they close the app and wait until the phone (that can easily get very hot and CPU get throttled) cools down?
- Considering that Std. is missing from the results reported in Table 1 and 2, I assume the authors did not repeat the experiment multiple times, and only reported performance for one run. This is very limited, performance can vary based on device state.
- Authors have only tested the evaluation on a single device (iPhone 14), and using a single on-device inference engine (llamacpp).
- Performance evaluations were only executed on CPU. It is possible to enable GPU support on llamacpp (through Metal in iOS) and performance should increase. Measuring Android would also be good (though not necessary), considering that you have an app ready.
- Power performance evaluation is limited to Battery Drained Rate, instead of energy or discharge.
- "Extensive experiments with MobileAIBench reveal several interesting findings. Quantization is an effective way to decrease model size while keeping the performance.". But, isn't that expected? Why it is presented as the first "interesting finding"?
- "we found 7B to be the upper limit of what a high-end phone’s hardware can manage (even after quantization)" 7B is not the generic upper limit, it is only the limit for the particular device. Also, I am not sure iPhone 14 can be considered as a high-end phone, without mentioning the Pro model that has more RAM memory and can possibly fit larger models.
- While manuscript writing quality is good, I have a few comments/suggestions:
  * Add a small summary explaining figures in its captions. There were moment that I had to move forward in order to understand them (e.g., Figure 1). 
  * Table 1 and 2: What is bold and what is underlined numbers?
  * "The first part is a pipeline for use on desktops or servers, to evaluate model performance on a specially selected set of widely known benchmarks.". Such as? Otherwise it looks too generic.

### Questions
- How did you access Battery Drained Rate, CPU usage, and memory while executing an experiment? Connecting the phone with a USB cable would interfere with the results. Were you connected over WiFi? This is an example of missing details of the methodology that was followed. 
- Have you run the experiment multiple times? If yes, what was the Std?
- How easy/hard is it to update the on-device inference engine in your pipeline?
- Have you measured performance while running the models in GPU?
- Are you planning to release the code in open source?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper conducts a benchmarking framework designed to evaluate the performance of large language models (LLMs) and large multimodal models (LMMs) on mobile devices, addressing the challenges of limited hardware resources. It consists of a desktop evaluation library and an iOS app, enabling comprehensive testing of quantized models across NLP, multimodal, and trust & safety tasks. MobileAIBench assesses models' efficiency, effectiveness, and resource utilization, providing insights into their feasibility for on-device deployment while supporting advancements in mobile AI research.

### Strengths
a) Real-world experiments.

b) By measuring latency and hardware resource usage on the iPhone 14, the study provides insights into the performance of smaller models.

c) The paper introduces an open-source tool that facilitates convenient testing of small models.

d) Writing is clear and fluency.

### Weaknesses
a) The experiments were conducted only on the iPhone 14, lacking evaluations on newer and more diverse devices. Currently, there are more mobile devices optimized specifically for on-device AI, such as the Snapdragon 8 Gen 3. Including these devices in testing would provide a more comprehensive view of model performance under different hardware conditions, offering broader insights for on-device AI applications.

b) In the section 4.3, the number of models tested is limited, failing to cover a wider variety of model architectures and parameter sizes. This limitation restricts a comprehensive understanding of how different models perform on mobile devices. Expanding the variety and scale of tested models would make the evaluation results more representative and valuable.

c) Although basic metrics such as performance, latency, and resource usage are provided, there is insufficient exploration of underlying reasons and optimization strategies. A more in-depth analysis would help us better understand the impact of different quantization levels and model architectures on task performance, offering valuable guidance for future research and practical deployment.

Detailed comments:
a) The paper shows that 3-bit quantization significantly reduces accuracy without lowering inference latency. This could be further analyzed, as extreme quantization may introduce computational complexities that offset latency benefits. 

b) The study only reports CPU results, but GPUs/XPUs are crucial for mobile AI tasks. Testing on these processors could reveal performance differences across hardware types, providing a fuller picture of deployment on mobile hardware. 

c) Despite Phi2’s larger model size, it has lower CPU utilization and faster inference than Gemma. Investigating Phi2’s architectural or parallelization optimizations could reveal design principles for high efficiency in on-device deployments.

d) Besides the mobile side, it is necessary to consider mobile-cloud-edge cooperation ways for better energy efficiency, e.g., Gearing Resource-Poor Mobile Devices with Powerful Clouds: Architecture, Challenges and Applications, iwc’13; TrimCaching: Parameter-sharing AI Model Caching in Wireless Edge Networks, icdcs’24, etc.

e) Although the paper notes that more output tokens increase Battery Drain Rate (BDR), this relationship isn’t clearly shown in Table 4.

### Questions
a) The experiments were conducted only on the iPhone 14, lacking evaluations on newer and more diverse devices. Currently, there are more mobile devices optimized specifically for on-device AI, such as the Snapdragon 8 Gen 3. Including these devices in testing would provide a more comprehensive view of model performance under different hardware conditions, offering broader insights for on-device AI applications.

b) In the section 4.3, the number of models tested is limited, failing to cover a wider variety of model architectures and parameter sizes. This limitation restricts a comprehensive understanding of how different models perform on mobile devices. Expanding the variety and scale of tested models would make the evaluation results more representative and valuable.

c) Although basic metrics such as performance, latency, and resource usage are provided, there is insufficient exploration of underlying reasons and optimization strategies. A more in-depth analysis would help us better understand the impact of different quantization levels and model architectures on task performance, offering valuable guidance for future research and practical deployment.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
A new benchmark is introduced to evaluate the behavior of LLMs and LMMs across various quantization levels, simulating deployment scenarios on mobile devices. By utilizing standard NLP, VQA, and safety tasks, the authors provide benchmarking references that offer insights into how model performance varies with quantization. The study highlights both the effectiveness and limitations of current quantization methods for LLMs. The limitation includes, for example, the need to address efficiency challenges in LMMs. The experimental findings underscore differences in performance across quantization levels, providing valuable information for developing more efficient algorithms.

The key contributions of this work are a novel benchmark regarding the quantization of LLM/LMMs, an open-source platform running on real devices, and in-depth analyses of the current quantization method and models.

### Strengths
S1 - This work makes a valuable contribution by expanding the community's understanding of models’ behaviors with quantization. This offers several analyses that will be beneficial for further research in this area, especially when deploying the model on mobile devices.

S2 - The open-sourced experimental platform is highly meaningful, allowing others to reproduce the work easily. 

S3 - For analyses, the authors have taken a comprehensive approach by considering various evaluation axes. For example, the studies on multimodal and safety tasks enhance the study’s relevance and depth.

### Weaknesses
W1 - The current set of tasks can be limited. With the growing interest in UI-based control for digital devices (such as Cluade-3.5 for computer use), it would be beneficial to include related tasks. Have the authors considered incorporating AndroidWorld (Rawles et al., 2024) for general capability assessment or MobileSafetyBench (Lee et al., 2024) for evaluating the safety of agents controlling mobile devices?

W2 - Relying solely on VQA for multimodal tasks may restrict the scope of analysis. Including other tasks, such as image captioning or OCR, could provide a more comprehensive evaluation of capabilities, especially considering their usage on mobile devices. The current VQA tasks do not fully explore the nuances of multimodal understanding required for complex mobile interactions, such as those involving spatial reasoning or fine-grained object recognition.

W3 - Although the authors’ choice of the iPhone-14 as a representative device is understandable, it would enhance the robustness of the study to consider other device types. For example, assessment with Android OS devices or tablets would provide a broader understanding. The performance characteristics of different mobile architectures (e.g., ARM vs. x86) and operating systems can significantly impact the effectiveness of quantization techniques, and limiting the evaluation to a single device may not generalize well.

W4 - (Minor) Certain aspects of the presentation could be improved. For example, the explanation of Figure 5 could be more detailed, and Figure 7 appears to be oddly rendered.

### Questions
Q1 - Could the authors clarify how this benchmark compares with existing ones regarding LLM quantization, such as LLM-QBench (Gong et al., 2024)? This comparison would help readers understand the unique contributions and positioning of this benchmark.

Q2 - What was the rationale behind selecting a random sample of 1,000 from the dataset? Justification of this choice, particularly regarding the representativeness and generalizability of the results, would be valuable.

Q3 - Could the authors explain why Llama-3.1-8B was not included in the experiment, considering it is only a 1B difference from the 7B models? Additionally, would the authors consider running supplementary experiments with the Llama-3.2 series (but I agree that adding these results may be infeasible, especially given its recent release) for offering valuable insights?

Q4 - In Figure 5, could the authors specify the meaning of the numbers on the y-axis? This clarification would aid in interpreting the results more accurately.

Q5 - Regarding Figure 5(b), it would be helpful if the authors could expand on this section in the main text, as the varying effects of quantization across task types could offer valuable insights.

Q6 - Could the authors provide possible explanations for why Moondream2 exhibited strong performance in 3-bit quantization, while other models did not achieve similar results?

Q7 - (Minor) In Appendix A.4, it appears that some of the table formats, particularly in Table 7, were rendered weirdly. The authors may want to review the formatting to ensure readability.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes MobileAIBench, a platform for evaluating the performance of large language models (LLMs) and multimodal models (LMMs) on mobile devices. MobileAIBench focuses on the task performance, resource consumption, and trust and security of quantized models on mobile devices. The authors have built testing tools for desktop and mobile platforms and explored the impacts of different quantization levels on task effectiveness and resource utilization through experiments. The platform has reference value in the mobile AI application scenarios.

### Strengths
**Comprehensive mobile AI testing platform**:  MobileAIBench integrates the existing benchmark testing framework for tasks and models. It is suitable for performance evaluation on end devices and fills the gap in mobile large model evaluation.

**Multi-dimensional performance evaluation**: The platform not only tests the performance of models on standard NLP and multimodal tasks, but also covers trust and security dimensions, highlighting privacy protection, bias, and ethical issues in mobile deployment.

**Real-device testing**:  MobileAIBench tests LLMs directly on mobile devices with key metrics such as latency, memory usage, CPU utilization, and battery consumption, which makes the results closer to actual application scenarios.

### Weaknesses
 **Insufficient mobile-side experiments**:  The focus of MobileAIBench should be on deploying LLMs and LMMs on mobile devices and examining the effects of quantization on task performance in these environments. However, most of the experiment results are from desktops rather than mobile devices. Supplementing with more mobile-side experiments, such as assessing the impacts of different quantization strategies (e.g., post-training quantization, quantization-aware training) and varying bit-widths (e.g., 4-bit, 8-bit) on mobile devices, would significantly strengthen the work. Specifically, the paper lacks a detailed analysis of how different quantization techniques affect the trade-off between model accuracy and resource consumption (latency, memory, power) on mobile platforms.

**Lack of data-level innovation**: MobileAIBench seems to be a collection of existing tasks and datasets without introducing specific data or design for benchmarking LLMs in mobile scenarios. As a benchmark, it lacks specialized datasets or test case designs tailored to mobile-specific scenarios, such as those involving intermittent network connectivity, limited input modalities (e.g., low-resolution camera input), or user interaction patterns unique to mobile devices. This limits the platform's ability to evaluate models under realistic mobile usage conditions. Thus, it may be more suitable to position MobileAIBench as a platform or testing tool rather than a standalone benchmark.

**Claims of device consistency require support**:  In line 235, the authors assert that test results on desktop devices are consistent with those on mobile devices. However, the paper does not provide sufficient experimental data, such as a direct comparison of performance metrics (e.g., accuracy, latency) for the same models and tasks across both desktop and mobile platforms, to support this claim. This lack of empirical validation undermines the credibility of the desktop-based results as proxies for mobile performance.

**Room for improvement in experimental design**:  Although the potential impacts of device temperature is mentioned (line 462), temperature should be included as a sub-metric in the evaluation metrics to better reflect real-world conditions on mobile devices. The paper should also consider the impact of other factors such as background processes, network conditions, and screen brightness on model performance and resource consumption. Furthermore, I still recommend to test on more mobile devices with varying hardware specifications (e.g., different CPU/GPU architectures, RAM sizes) to obtain more persuasive and generalizable results.

### Questions
Can the authors provide more discussions and justifications for the above?

### Soundness
3

### Presentation
3

### Contribution
2
