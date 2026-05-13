# Revisiting DNN Training for Intermittently-Powered Energy-Harvesting Micro-Computers

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The deployment of Deep Neural Networks (DNNs) in energy-constrained environments, such as Energy Harvesting Wireless Sensor Networks (EH-WSNs), presents unique challenges, primarily due to the ``intermittent'' nature of power availability. To address these challenges, this study introduces and evaluates a novel training methodology tailored for DNNs operating within such contexts. In particular, we propose a dynamic dropout technique that adapts to both the architecture of the device and the variability in energy availability inherent in energy harvesting scenarios. 

Our proposed approach leverages a device model that incorporates specific parameters of the network architecture and the energy harvesting profile to optimize dropout rates dynamically during the training phase. By modulating the network’s training process based on predicted energy availability, our method not only conserves energy but also ensures sustained learning and inference capabilities under power constraints. Our preliminary results demonstrate that this strategy provides $6\%$ -- $22\%$ accuracy improvements compared to the state of the art with $\le 5\%$ additional compute. This paper details the development of the device model, describes the integration of energy profiles with intermittency aware dropout and quantization algorithms, and presents a comprehensive evaluation  of the proposed approach using real-world energy harvesting data. The work also includes a new dataset towards deploying energy harvesting based computation in real world.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces NExUME, a framework addressing issues with DNN training for energy-constrained environments which can't guarantee a sufficient amount of power at all times, such as Energy Harvesting Wireless Sensor Networks. In order to optimise DNN-Training for these unstable conditions, NExUME relies on an estimation of the available resources. For this, a first-of-its-kind dataset containing energy harvesting traces and available computation libraries is introduced.
The training process reduces intermittency-related failures by treating the number of loop iterations as learnable parameters and task-fusions to meet energy budgets. Additionally, dynamic dropouts during execution ensure the completion of layers and dynamic quantization balances out the accuracy degradation. An adaptive regularization strategy prevents weights from being undertrained. Lastly, the authors introduce a task-scheduler that adjusts in real-time to the energy conditions estimated.

### Strengths
- Embedding energy variability into the training process is a novel idea.
- Extends existing Neural Architecture Search for intermittent computing systems
- Evaluation on SOTA datasets and DNNs (in the context of intermittent computing)

### Weaknesses
 - Evaluation on SOTA datasets and DNNs (in the context of intermittent computing). While also a strength, it also raises a questions. The ML community has moved on to Attention and Transformers and large scale datasets. This paper does not discuss how such modern architectures can be deployed in the intermittent setting.

- contribution over SOTA remains unclear. The paper cites numerous NAS frameworks for intermittent/MCU computing (and there are more like [1]) and a large body of work on intermittent execution of DNNs such as [2, 3] and numerous papers cited in the introduction. To me, the contribution over these remains unclear, as many aspects are also in these papers. 

- lack of SOTA baselines: The paper should compare to SOTA approaches. 

- statement such as "Since we are the first work to propose a new training approach targeted for intermittent devices and inference optimizations" should be toned down. Instead, please carefully explain your contributions over SOTA and compare them to SOTA baseline. 

- ablation study: accuracy and overhead if full power is available 

- Overall: this paper is better suited at a system conference, such as SenSys or MobiSys

- the title is misleading, the paper is about more than DNN training. 

- BLE board does not have FeRAM and thereby not a classic board for intermittent computing. Why do the authors choose it? How does the intermittent part work here, especially QuantaTask?


-  On several occurrences, the paper is written (too) vaguely. E.g. 
      - There is no hint as to how tasks are "fused" when executing multiple quanta would exceed the energy budget. To my understanding, the function in only explained in the appendix as part of the source code but not the text.
      -  Dropout rates are adjusted on "specific" criteria. Even though the appendix provides details, this vague style of writing reads weirdly and is better served with examples

- As mentioned on several occasions, a big part of the presented work is the availability of the database of DynAgent which also contains hardware-information, yet only 2 different microcontrollers are used for evaluating the framework. Testing a broader variety of systems seems sensible here

- Drawbacks like up to 34% increased instruction count and up to 17% increased memory bandwidth usage are stated but hardly discussed or put into perspective. While this is not surprising for intermittent computing, the numbers should still be discussed and be compared to other approaches.

- Typos: Figure 3: Sensitivity and ablation study. DN is DynNAS, DF is FynFit, and DI is DynInfer: FynFit -> DynFit

- with a Pixel-5 phone as the host device: does this matter? Any device should do the job.

- the paper has a section LIMITATIONS AND DISCUSSION which also discussed limitations, such as the runtime overhead. The last two sentences, however, read a bit bumpy and should be streamlined and also discussed (and not just stated).

### Questions
* the BLE board does not have FeRAM and thereby not a classic board for intermittent computing. Why do the authors choose it? How does the intermittent part work here, especially QuantaTask?

* what are the contributions over SOTA?

* what is the performance compared SOTA baselines?

* can you consider a different title?

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
4

### Summary
The paper introduces a framework designed to enable consistent and accurate deep neural network inference on energy-harvesting wireless sensor networks that operate under intermittent power conditions. This framework addresses the challenges of unreliable energy supply and computational limitations in such environments. The proposed framework uses energy variability aware network architecture search, dynamic training optimizations, and an intermittency-aware task scheduler to adapt DNN computations based on real-time energy availability, in order to meet service level objectives (SLOs) in resource-constrained settings.

### Strengths
The paper studies an interesting and important problem of enabling reliable DNN inference in energy-harvesting wireless sensor networks. The writing is overall clear and well-organized. The motivations, methods, and experimental findings are easy to follow.

### Weaknesses
The proposed method relies on detailed profiling of the hardware to model energy consumption, computational capabilities, and memory footprint. This process can be time-consuming and complex, requiring extensive micro-profiling, and the paper does not sufficiently address the practical challenges of performing this profiling across diverse hardware platforms. The reliance on accurate energy models, which are derived from this profiling, makes the entire framework sensitive to errors in these models. 

In DynInfer, an energy-aware priority scheduling heuristic is used. With no theoretical analysis of its performance compared to an optimal scheduling solution, its scheduling optimality is hard to estimate. The paper lacks a rigorous analysis of the heuristic's performance bounds, making it difficult to assess its effectiveness in various scenarios. The heuristic's performance could degrade significantly under different energy availability patterns or task arrival rates, which are not explored in detail.

The explanations of some techniques in the methods section, particularly within the DynFit and DynInfer components, remain at a high level, lacking depth in technical specifics. For example, while the dynamic dropout and quantization strategies in DynFit are introduced, there is limited detail on how dropout rates and quantization levels are adjusted based on energy profiles, such as the specific algorithms or mathematical formulations used, or how these adjustments differ from standard implementations. Additionally, the methods used in each component lack a sense of innovation, as they seem to be a simple use of existing techniques without substantial enhancements. The paper does not clearly articulate the novel aspects of the proposed approach compared to existing dynamic adaptation techniques.

The impact of under-trained and overfitting weights requires further examination. More frequent updates of certain weights do not necessarily lead to "overfitting," and, conversely, infrequent updates do not inherently imply "underfitting." From a layer perspective, the effect of varying update frequencies on individual weights may be limited, suggesting that this issue may be less impactful than indicated. The paper does not provide a clear justification for how the proposed weight update strategy effectively mitigates underfitting or overfitting.

The experiments mainly focus on accuracy improvement. Other performance metrics, such as energy consumption, latency, computational overhead, and the number of power failures or SLO violations, are not extensively analysed. The paper lacks a comprehensive evaluation of the trade-offs between accuracy and other critical performance metrics in energy-harvesting environments. The experiments are conducted on relatively small datasets and models, which limits the generalizability of the findings to more complex, real-world applications.

### Questions
1. How much of the resource of the method is used or what is its time complexity?

2. As a sub-optimal scheduling solution, how would its scheduling performance to be ensured?

3. What is the rationale behind the overall method design?

4. Whether the accuracy is more important than the other performance metrics in your design?

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
4

### Summary
The paper presents NExUME, a novel framework for training and deploying deep neural networks (DNNs) on energy-harvesting micro-computers with intermittent power. The authors introduce dynamic dropout rates and quantization levels that adapt based on real-time energy availability, improving the accuracy and robustness of DNNs in constrained power settings. The paper demonstrates NExUME's efficacy in optimizing both training and inference phases through extensive experiments, showcasing significant accuracy gains over traditional approaches in intermittently powered environments. Additionally, the introduction of a unique dataset to facilitate further research on energy-harvesting applications is a noteworthy contribution.

### Strengths
1. The paper addresses an important challenge in deploying DNNs on resource-constrained, intermittently powered devices, an area that is underexplored in current literature. By incorporating real-time energy-aware adaptations, this work proposes a unique and valuable solution.
2. The work is thorough, presenting a well-structured methodology, clearly defined optimization functions, and a series of experiments across various datasets and hardware platforms. The choice of energy-aware dropout and quantization strategies tailored to intermittent environments is both innovative and well-validated.
3. The paper is well-written, with each component of the proposed framework (DynFit, DynInfer) and the optimization strategies clearly explained. Figures and tables effectively support the results and comparisons.
4. The proposed approach has broad implications for real-world applications in energy-limited environments, such as remote monitoring and IoT systems, where consistent power is unavailable. The improvements in accuracy (6-22%) and the novel dataset enhance the significance and impact of the research.

### Weaknesses
1. The experiments, while comprehensive, rely on specific hardware configurations that may not be accessible for replication. The reliance on components like MSP430FR5994 and certain energy-harvesting setups may limit reproducibility. Specifically, the paper lacks details on the energy harvesting source characteristics (e.g., solar panel size, light intensity, or vibration frequency) and how these affect the observed performance. This makes it difficult to assess the generalizability of the results to other energy harvesting scenarios.
2. While the paper compares NExUME to iNAS and other energy-aware methods, it lacks a detailed comparison with additional state-of-the-art adaptive or intermittent DNN training techniques. The comparison is limited to a few selected methods, and a more comprehensive benchmark against a wider range of approaches, including those focused on model compression and dynamic resource allocation, is needed to fully validate the superiority of the proposed method.
3. The paper mentions challenges with larger networks and datasets. However, there is limited discussion on potential approaches to address these limitations, which would be valuable for practitioners aiming to scale this approach. For instance, the paper does not explore techniques like model parallelism or distributed training, which could mitigate the resource constraints when dealing with larger models. Furthermore, the impact of increased model complexity on the dynamic adaptation mechanisms is not discussed.
4. The profiling is based on conservative estimates, which, while practical, may not be universally applicable. The paper does not provide a detailed analysis of how these conservative estimates were derived, nor does it explore the sensitivity of the system to variations in these estimates. The impact of over- or under-estimating energy availability on the model's performance and stability is not clearly addressed.

### Questions
1. Can the authors clarify the robustness of NExUME across various hardware platforms beyond those tested? Would modifications be required for different types of microcontrollers or energy-harvesting setups?
2. How does NExUME handle environments with extremely low or sporadic energy levels, where consistent dropout and quantization adjustments may not be feasible?
3. Can the authors provide more detail on the potential effects of overfitting introduced by DynFit’s dropout variations? Would techniques like dropout scheduling help mitigate this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents NExUME, a training methodology that is designed to cater to intermittent power energy harvesting systems.   The authors proposed two key contributions which are (1) a new method for training where one can dynamically adjust dropout rate and quantization levels to cater to varying energy availability in the EH system, and (2) a task scheduler that optimizes task completion in EH systems. The authors also contribute a machine status monitoring dataset. NExUME shows a 6 to 22 % accuracy improvement over existing baselines on simple ML tasks. However, at the same time, NExUME incurs a 5% overhead in computation, an increase in the number of instructions ranging between  11.4%-  34.2%, and an increase in memory bandwidth from 6 to 17%.

### Strengths
+ This paper is the first to present novel training and inference methods that take dropouts and quantization into account in the context of energy harvesting systems. 
+ A new machine monitoring dataset 
+ The results shown are good when compared to the baselines presented in the paper.
+ Writing and the presentation of the work are clear. 
+ Choice of datasets is appropriate given that the work is designed for resource-constrained embedded systems. 
+ Decent ablation studies 
+ Actual implementation of such a system is not trivial.

### Weaknesses
 - The idea of dynamically adjusting dropout rates and quantization levels is not novel. It is novel in the context of EH systems. 
- Energy-aware scheduling is not novel. 
- The quantification of overheads is done. However, its implications are not discussed. The range in terms of % is indicated. However, how does it vary with the datasets? 
- Some of the existing work in intermittent systems are not compared such as ePerceptive: energy reactive embedded intelligence for batteryless sensors and Zygarde: Time-Sensitive On-Device Deep Inference and Adaptation on Intermittently-Powered Systems
- Details on the machine status monitoring dataset are missing in Sec 4.3 How are R1, R2, and R3 different? What are their RPM speeds? What is S1 and S2? 
- Only accuracy results are shown.  It is also important to know the latency/inference. and memory requirements of the system. 
- DynFit comprises adjusting quantization levels and dropouts. In the ablation studies, it is unclear which of these is bringing more benefits to the system.

### Questions
Details on the machine status monitoring dataset are missing in Sec 4.3 How are R1, R2, and R3 different? What are the RPM speeds? What is S1 and S2?

Energy-aware scheduling is not novel. Can you clarify your novelty with respect to existing scheduling algorithms? 

The authors claim that their machine status monitoring is the first of its kind. Can they clarify what datasets already exist and how the dataset introduced in the paper is different?

### Soundness
3

### Presentation
3

### Contribution
2
