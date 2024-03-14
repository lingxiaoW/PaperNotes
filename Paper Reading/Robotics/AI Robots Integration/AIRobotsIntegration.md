# AI Robotics Integration

## LLM-based Agent Review Collection:
* [Efficient LLMs: A Survey](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey)
* [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics?tab=readme-ov-file)
* [Awesome-Implicit-NeRF-Robotics](https://github.com/zubair-irshad/Awesome-Implicit-NeRF-Robotics?tab=readme-ov-file)


---

## Terminologies

- **[Grounding](./ARI_Notes/grounding.md)**
- **[Open-Vocabulary & Closed-Vocabulary](./ARI_Notes/open_vocabulary.md)**

---


## Review Articles

- **Robots that use language** [(pdf)](./Robots%20that%20use%20language.pdf) (Citation: 211)


---

## Simulation Environments
* **Remote Object Grounding**:
  * [REVERIE](https://github.com/YuankaiQi/REVERIE)
* **Housekeeper environment**:
  * [ALFRED](https://askforalfred.com/)
  * [Minedojo](https://github.com/MineDojo/MineDojo)
  * [SOON](https://scenario-oriented-object-navigation.github.io/)
* **Environment Understanding:**
  * [OpenScene](https://github.com/pengsongyou/openscene)
  * [ScanRefer](https://daveredrum.github.io/ScanRefer/)
* **Object Manipulation:**
  * [RAVENS](https://github.com/google-research/ravens?tab=readme-ov-file)
* **Humanoid Robot:**
  * [Issac Gym](https://developer.nvidia.com/isaac-gym)

---

## Useful Sentences
* It has been well-established that language acts as a valuable interface fro non-experts to communicate with robots [cite: toward understanding natural language directions 2010]. 

---

## Object Manipulation
- **GAPartNet Cross-Category Domain-Generalizable Object Perception and
  Manipulation via Generalizable and Actionable Parts**
 **[`CVPR 2023`]** *Haoran Geng, Helin Xu, Chengyang Zhao, Chao Xu, Li Yi, Siyuan Huang, He Wang* [(arXiv)](http://arxiv.org/abs/2211.05272) [(pdf)](./GAPartNet%20Cross-Category%20Domain-Generalizable%20Object%20Perception%20and%20Manipulation%20via%20Generalizable%20and%20Actionable%20Parts.pdf) [(Note)](./ARI_Notes/GAPartNet.md) (Citation: 8)
  - Propose a **G**eneralizable and **A**ctionable **Parts** (GAParts)


---

## Robotic Transformer


### 2022

- **A Generalist Agent** **[`arXiv 2022`]** *Scott Reed, et al.* [(arXiv)](http://arxiv.org/abs/2205.06175) [(pdf)](./A%20Generalist%20Agent.pdf) [(Notes)](./ARI_Notes/AGeneralistAgent.md)(Citation: 393)
  - Gato is a multi-modal, multi-task, multi-embodiment generalist policy

<br />

- **SayCan: Do As I Can Not As I Say Grounding Language in Robotic Affordances**
 **[`arXiv 2022`]** *Michael Ahn, Anthony Brohan, et al.* [(arXiv)](http://arxiv.org/abs/2204.01691) [(pdf)](./SayCan%20-%20Do%20As%20I%20Can%20Not%20As%20I%20Say.pdf)[(Notes)](./ARI_Notes/saycan.md) (Citation: 411)
  - Saycan: provide **real-world grounding** that links the LLM and robotic tasks.


<br>

- **RT-1 Robotics Transformer for Real-World Control at Scale** **[`arXiv 2022`]** *Anthony Brohan, et al.* [(arXiv)](http://arxiv.org/abs/2212.06817) [(pdf)](./rt1%20-%20robotics%20transformer%20for%20real-world%20control%20at%20scale.pdf) [(Notes)](./ARI_Notes/rt1.md) (Citation: 107)
  - Trained a robotic Transformer that converts human instructions into robot actions. 


<br>

- **Code as Policies Language Model Programs for Embodied Control**
 **[`arXiv 2022`]** *Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, Andy Zeng* [(arXiv)](http://arxiv.org/abs/2209.07753) [(pdf)](./Code%20as%20Policies%20Language%20Model%20Programs%20for%20Embodied%20Control.pdf) [(Notes)](./ARI_Notes/code_as_policy.md) (Citation: 300)
    - Use LLM to generate robot policy code from natural language commands

<br>

- **Inner Monologue Embodied Reasoning through Planning with Language
  Models**
 **[`arXiv 2022`]** *Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, Pierre Sermanet, Noah Brown, Tomas Jackson, Linda Luu, Sergey Levine, Karol Hausman, Brian Ichter* [(arXiv)](http://arxiv.org/abs/2207.05608) [(pdf)](./Inner%20Monologue%20Embodied%20Reasoning%20through%20Planning%20with%20Language.pdf) [(Notes)](./ARI_Notes/inner_monologue.md) (Citation: 456)
    - Convert environmental information as texts to continuosly inject information to a LLM, forcing it to generate a plan. 


<br>

### 2023
 - **ChatGPT for Robotics Design Principles and Model Abilities**
 **[`arXiv 2023`]** *Sai Vemprala, Rogerio Bonatti, Arthur Bucker, Ashish Kapoor* [(arXiv)](http://arxiv.org/abs/2306.17582) [(pdf)](./ChatGPT%20for%20Robotics%20-%20Design%20Principles%20an%20Model%20Abilities.pdf) (Citation: 62)
    - A framework of using ChatGPT to generate robot action plans.  



<br />

- **RT-2 Vision-Language-Action Models Transfer Web Knowledge to Robotic
  Control** **[`arXiv 2023`]** *Anthony Brohan, et al.* [(arXiv)](http://arxiv.org/abs/2307.15818) [(pdf)](./rt2%20-%20vision-language-action%20models%20transfer%20web%20knowledge%20to%20robotic%20control.pdf)[(Notes)](./ARI_Notes/rt2.md) (Citation: 6)
  - Treat actions as text tokens.
<br />


- **Open X-Embodiment Robotic Learning Datasets and RT-X Models**
 **[`arXiv 2023`]** *Open X-Embodiment Collaboration* [(arXiv)](http://arxiv.org/abs/2310.08864) [(pdf)](./Open%20X-Embodiment%20Robotic%20Learning%20Datasets%20and%20RT-X%20Models.pdf) [(Notes)](./ARI_Notes/open_x.md)(Citation: 39)
  - An open-source dataset for robot trajectories.


<br />

- **VIMA General Robot Manipulation with Multimodal Prompts**
 **[`ICML 2023`]** *Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen, Li Fei-Fei, Anima Anandkumar, Yuke Zhu, Linxi Fan* [(arXiv)](http://arxiv.org/abs/2210.03094) [(Notes)](./ARI_Notes/vima.md) [(pdf)](./VIMA%20-%20General%20Robot%20Manipulation%20with%20Multimodal%20Prompts.pdf) (Citation: 53)



<br />

- **PaLM-E An Embodied Multimodal Language Model**
 **[`arXiv 2023`]** *Danny Driess, Fei Xia, et al.* [(arXiv)](http://arxiv.org/abs/2303.03378) [(pdf)](./palm-e.pdf)[(Notes)](./ARI_Notes/palm-e.md) (Citation: 194)
  - A LLM-based agent that generates robot actions as textual instructions to perform. 


<br />

- **Learning Humanoid Locomotion with Transformers**
 **[`arXiv 2023`]** *Ilija Radosavovic, Tete Xiao, Bike Zhang, Trevor Darrell, Jitendra Malik, Koushil Sreenath* [(arXiv)](http://arxiv.org/abs/2303.03381) [(pdf)](./Learning%20Humanoid%20Locomotion%20with%20Transformers.pdf) [(Notes)](./ARI_Notes/humanoid_transformer.md)(Citation: 6)
  - Use a causal transformer model to control a humanoid locomotion.

<br />



- **Towards End-to-End Embodied Decision Making via Multi-modal Large
  Language Model Explorations with GPT4-Vision and Beyond**
 **[`arXiv 2023`]** *Liang Chen, Yichi Zhang, Shuhuai Ren, Haozhe Zhao, Zefan Cai, Yuchi Wang, Peiyi Wang, Tianyu Liu, Baobao Chang* [(arXiv)](http://arxiv.org/abs/2310.02071) [(pdf)](./Towards%20End-to-End%20Embodied%20Decision%20Making%20via%20Multi-modal%20Large%20Language%20Model%20-%20Explorations%20with%20GPT4-Vision%20and%20Beyond.pdf) [(Notes)](./ARI_Notes/PCA-EVAL.md) (Citation: 0)


 <br>

 - **VoxPoser Composable 3D Value Maps for Robotic Manipulation with
  Language Models**
 **[`arXiv 2023`]** *Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, Li Fei-Fei* [(arXiv)](http://arxiv.org/abs/2307.05973) [(pdf)](./VoxPoser%20Composable%203D%20Value%20Maps%20for%20Robotic%20Manipulation%20with%20LLMs.pdf) (Citation: 98)


  

<br >

- **Voyager An Open-Ended Embodied Agent with Large Language Models**
 **[`arXiv 2023`]** *Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar* [(arXiv)](http://arxiv.org/abs/2305.16291) [(pdf)](./Voyager%20An%20Open-Ended%20Embodied%20Agent%20with%20Large%20Language%20Models.pdf) [(Notes)](./ARI_Notes/voyager.md) (Citation: 254)
    - **Voyager** is the **first LLM-powered embodied lifelong learning agent** that operates within the virtual realm of **Minecraft**.
    - It continuously **explores the Minecraft world**, acquires a diverse range of skills, and makes novel discoveries—all without any human intervention.





---

## Object Grounding

- **RREx-BoT Remote Referring Expressions with a Bag of Tricks**
 **[`arXiv 2023`]** *Gunnar A. Sigurdsson, Jesse Thomason, Gaurav S. Sukhatme, Robinson Piramuthu* [(arXiv)](http://arxiv.org/abs/2301.12614) [(pdf)](./RREx-BoT%20Remote%20Referring%20Expressions%20with%20a%20Bag%20of%20Tricks.pdf)[(Notes)](./ARI_Notes/rrex-bot.md) (Citation: 0)
  - Using a generic vision-language scoring model with minor modifications for 3D encoding and operating in an embodied environment. 


<br />

- **LLM-Grounder Open-Vocabulary 3D Visual Grounding with Large Language
  Model as an Agent**
 **[`arXiv 2023`]** *Jianing Yang, Xuweiyi Chen, Shengyi Qian, Nikhil Madaan, Madhavan Iyengar, David F. Fouhey, Joyce Chai* [(arXiv)](http://arxiv.org/abs/2309.12311) [(pdf)](./LLM-Grounder%20-%20Open-Vocabulary%203D%20Visual%20Grounding%20with%20Large%20Language%20Model%20as%20an%20Agent.pdf)[(Notes)](./ARI_Notes/llm_grounder.md) (Citation: 8)
  -  Focus on 3D visual object grounding. Let the robot to understand 3D objects. 
  -  Use LLM to decompose complex natural language queries into semantic constitutents and employs a visual grounding tool to identify objects in a 3D scene. 
    

<br />

---



## Prompt Engineering

- **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**
 **[`arXiv 2022`]** *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou* [(arXiv)](http://arxiv.org/abs/2201.11903) [(pdf)](./chain-of-thought.pdf) [(Notes)](./ARI_Notes/cot.md) (Citation: 1241)
  - Generate a **chain of thought**, i.e., a series of intermediate reasoning steps, to significantly improve the ability of large language models to perform complex reasoning.


<br>

- **ProgPrompt Generating Situated Robot Task Plans using Large Language
  Models** **[`arXiv 2022`]** *Ishika Singh, Valts Blukis, Arsalan Mousavian, Ankit Goyal, Danfei Xu, Jonathan Tremblay, Dieter Fox, Jesse Thomason, Animesh Garg* [(arXiv)](http://arxiv.org/abs/2209.11302) [(pdf)](./ProgPrompt%20Generating%20Situated%20Robot%20Task%20Plans%20using%20Large%20Language.pdf) [(Notes)](./ARI_Notes/progprompt.md) (Citation: 271)

  - This work introduces situated awareness in LLM-based robot task planning.

<br>

- **Large Language Models are Zero-Shot Reasoners**
 **[`NeurIPS 2022`]** *Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, Yusuke Iwasawa* [(arXiv)](http://arxiv.org/abs/2205.11916) [(pdf)](./Large%20Language%20Models%20are%20Zero-Shot%20Reasoners.pdf) [(Notes)](./ARI_Notes/llm_zeroshot.md) (Citation: 1483)
  - Simply add "Let's think step by step" before each answer can achieve few-shot learning. 

---

## In Context Learning

- **A Survey on In-context Learning**
 **[`arXiv 2022`]** *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu, Lei Li, Zhifang Sui* [(arXiv)](http://arxiv.org/abs/2301.00234) [(pdf)](./A%20Survey%20on%20In-context%20Learning.pdf) [(Notes)](./ARI_Notes/surveyICL.md) (Citation: 445)

---

## Vision-based Navigation

- **BADGR An Autonomous Self-Supervised Learning-Based Navigation System**
 **[`arXiv 2020`]** *Gregory Kahn, Pieter Abbeel, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2002.05700) [(pdf)](./BADGR%20-%20An%20Autonomous%20Self-Supervised%20Learning-Based%20Navigation%20System.pdf) (Citation: 230)


<br />

- **ViNG Learning Open-World Navigation with Visual Goals**
 **[`ICRA 2021`]** *Dhruv Shah, Benjamin Eysenbach, Gregory Kahn, Nicholas Rhinehart, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2012.09812) [(pdf)](./ViNG%20-%20Learning%20Open-World%20Navigation%20with%20Visual%20Goals.pdf) [(Notes)](./ARI_Notes/ving.md) (Citation: 66)
    - Propose a learning-based navigation system for reaching visually indicated goals and demonstrate this system on a real mobile robot platform.   
  
<br />

- **GNM: A General Navigation Model to Drive Any Robot**
 **[`ICRA 2023`]** *Dhruv Shah, Ajay Sridhar, Arjun Bhorkar, Noriaki Hirose, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2210.03370) [(pdf)](./GNM%20-%20A%20General%20Navigation%20Model%20to%20Drive%20Any%20Robot.pdf) [(Notes)](./ARI_Notes/gnm.md) (Citation: 35)
  - **Overall:** this is a follow-up work of the ViNG, which proposes a universal model for vision-based navigation on multiple robotic platforms.


<br />

- **LM-Nav Robotic Navigation with Large Pre-Trained Models of Language
  Vision and Action**
 **[`arXiv 2022`]** *Dhruv Shah, Blazej Osinski, Brian Ichter, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2207.04429) [(pdf)](./LM-Nav%20-%20Robotic%20Navigation%20with%20Large%20Pre-Trained%20Models%20of%20Language,%20Vision,%20and%20Action.pdf) [(Notes)](./ARI_Notes/lm-nav.md) (Citation: 160) 
    - Enable a self-supervised system for robotic navigation to execute natural language instructions by leveraging the capabilities of pre-trained models without any user-annotated navigational data. 
    - This method uses LLMs to construct an interface that humans can use to communicate desired tasks to robots. 

<br />

- **FastRLAP A System for Learning High-Speed Driving via Deep RL and
  Autonomous Practicing**
 **[`arXiv 2023`]** *Kyle Stachowicz, Dhruv Shah, Arjun Bhorkar, Ilya Kostrikov, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2304.09831) [(pdf)](./FastRLAP%20-%20A%20System%20for%20Learning%20High-Speed%20Driving%20via%20Deep%20RL%20and%20Autonomous%20Practicing.pdf) [(Notes)](./ARI_Notes/fastrlap.md) (Citation: 3)
  - **Objective**: Design a deep learning model to control a RC car to drive aggressively from visual observations using reinforcement learning.
 
  


