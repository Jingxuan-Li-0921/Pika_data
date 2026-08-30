

**版本变更记录：**

| <font style="color:#333333;">版本</font> | <font style="color:#333333;">信息变更</font> | <font style="color:#333333;">变更人</font> | <font style="color:#333333;">审核人</font> | <font style="color:#333333;">时间</font> |
| :---: | --- | :---: | :---: | --- |
| <font style="color:#333333;">V1.0.0</font> | <font style="color:#333333;">文档建立</font> | <font style="color:#333333;">Dennis</font> | | <font style="color:#333333;">20250103</font> |
| <font style="color:#333333;">V1.</font><font style="color:#333333;">1</font><font style="color:#333333;">.</font><font style="color:#333333;">0</font> | <font style="color:#333333;">文档修正</font> | <font style="color:#333333;">Dennis</font> | | <font style="color:#333333;">20250401</font> |
| <font style="color:#333333;">V1.1.1</font> | <font style="color:#333333;">文档修正：</font><br/><font style="color:#333333;">增加同一空间多套设备基站安装方法</font> | <font style="color:#333333;">Dennis</font> | | <font style="color:#333333;">20250410</font> |
| <font style="color:#333333;">V1.1.2</font> | 文档修正   增加手册使用指引<br/>增加使用流程说明<br/>增加使用QA<br/>修改指示灯及按键功能 | Dennis | | 20250523 |
| <font style="color:#333333;">V1.1.3</font> | 文档修正   修改 Sense 状态指示灯含义 | Dennis | | 20250605 |
| <font style="color:#333333;">V1.1.4</font> | 文档修正   增加修正摇操部分代码 | Dennis | | 20250609 |
| <font style="color:#333333;">V1.1.5</font> | 文档修正<br/>修正遥操作环境依赖 | RoboPPN | | 20250611 |
| <font style="color:#333333;">V1.1.6</font> | 文档修正<br/>增加基站供电充电说明<br/>增加 sense/gripper 相机与夹爪相对位置尺寸图 | Dennis | | 20250613 |


# **<font style="color:#1a1a1a;">手册使用指引：</font>**
<font style="color:#333333;">PIKA-SENSE</font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442562556-ab518b01-06e7-4686-b862-3df945556cea.png" width="72" title="" crop="0,0,1,1" id="uaa5f92e2" class="ne-image"><font style="color:#333333;">PIKA-GRIPPER </font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442562636-6ad9baf4-ed6c-4094-a205-5a7d51bc7151.png" width="65" title="" crop="0,0,1,1" id="u899c7d26" class="ne-image"><font style="color:#333333;"> PIKA-STATION </font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442562679-d3e2f5c0-c87c-4ed8-a4f5-1ebf11d19971.png" width="25" title="" crop="0,0,1,1" id="u97155c64" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1747971444386-8f718de1-9053-47e4-80fb-b794f22fcef7.png?x-oss-process=image%2Fformat%2Cwebp" width="1031" title="" crop="0,0,1,1" id="NkJFv" class="ne-image">

# **<font style="color:#1a1a1a;">Pika手持采集使用指引：</font>**
**<font style="color:#333333;">单独使用Pika Sense与Pika Station搭配，进行手持式数据采集</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442563815-9c641931-fac9-4c8a-9044-09c1ad83a682.png" width="750" title="" crop="0,0,1,1" id="u15bedff6" class="ne-image">

:::warning
**<font style="color:#333333;">图示说明：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">黑色实线为有线连接</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">灰色虚线为非实际线束，仅代表信号传输</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">蓝色箭头表示需要端口实际接入</font>

**<font style="color:#333333;">操作简易步骤概述：</font>**

<font style="color:#333333;">1-基站搭建（基站连接电池或使用适配器连接电源）</font><font style="color:#333333;">2-调节基站，确保Pika Sense在两个基站覆盖范围内，无遮挡</font>

<font style="color:#333333;">3-Pika Sense Type-C线束USB口连接PC(必须使用USB3.0端口，插入后请勿更换）</font>

<font style="color:#333333;">4-USB无线接收器使用Windows系统下SteamVR软件进行初次配对（仅一次），</font>**<font style="color:#333333;">Sense绿灯常亮则配对成功</font>**

<font style="color:#333333;">5-软件操作：PC 软件环境部署（参照部署2.4）</font>

<font style="color:#333333;">6-软件操作：Pika Station校准，软件校准，</font>**<font style="color:#000000;">TF跟随Sense变化则校准成功</font>**

<font style="color:#333333;">7-软件操作：单Sense即可开启采集</font>

<font style="color:#333333;">8-软件操作：双Sense使用，需先配置左右手及左右相机，再开启采集</font>

:::

# **<font style="color:#1a1a1a;">Pika-Gripper单独使用指引：</font>**
**<font style="color:#333333;">单独使用Pika Gripper进行推理执行（将Gripper作为单独的夹爪进行使用）</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442563879-c5b3fdcc-a1d8-4fb5-b63e-0990187dd009.png" width="602" title="" crop="0,0,1,1" id="u45ccaef0" class="ne-image">

:::warning
**<font style="color:#333333;">图示说明：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">黑色实线为有线连接</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">蓝色箭头表示需要端口实际接入</font>

**<font style="color:#333333;">操作简易步骤概述：</font>**

<font style="color:#333333;">1-设计法兰，结构组装</font>

<font style="color:#333333;">2-电器连接组装（机械臂供电及Gripper供电）</font>

<font style="color:#333333;">3-通讯连接，Gripper后部Tpye-C接口连接PC</font>

<font style="color:#333333;">4-软件操作：PC 配置ROS驱动（参照5.4部署）</font>

<font style="color:#333333;">5-软件操作：开始控制使用</font>

:::

# **<font style="color:#1a1a1a;">Pika 摇操机械臂使用指引：</font>**
**<font style="color:#333333;">Pika 遥操采集（默认使用Piper两指夹爪，Gripper适配中，可搭配其他任意臂进行遥操作）</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442563829-3033bf82-2110-45b2-883c-a606bb46f468.png" width="793" title="" crop="0,0,1,1" id="u3f25a5e3" class="ne-image">

:::warning
**<font style="color:#333333;">图示说明：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">黑色实线为有线连接</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">灰色虚线为非实际线束，仅代表信号传输</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">蓝色箭头表示需要端口实际接入</font>

**<font style="color:#333333;">操作简易步骤概述：</font>**

<font style="color:#333333;">1-基站搭建（基站连接电池或使用适配器连接电源）</font><font style="color:#333333;">2-调节基站，确保Pika Sense在两个基站覆盖范围内，无遮挡</font>

<font style="color:#333333;">3-Pika Sense Type-C线束USB口连接PC(必须使用USB3.0端口，插入后请勿更换）</font>

<font style="color:#333333;">4-USB无线接收器使用Windows系统下SteamVR软件进行初次配对（仅一次），Sense绿灯常亮则配对成功</font>

<font style="color:#333333;">5-机械臂组装，完成供电，测试机械臂本体运动正常</font>

<font style="color:#333333;">6-机械臂通信连接PC（如使用PIPER则将USB-CAN的USB口连接至PC）</font>

<font style="color:#333333;">7-软件操作：PC 软件环境部署(参照部署2.4)</font>

<font style="color:#333333;">8-软件操作：Pika Station校准，软件校准，TF跟随Sense变化则校准成功</font>

<font style="color:#333333;">9-软件操作：摇操软件部署(参照部署6.2)</font>

<font style="color:#333333;">10-软件操作：单Sense摇操即可启动，双Sense摇操，先配置左右手及左右相机，再开启摇操</font>

:::

# **<font style="color:#1a1a1a;">重要安全信息 </font>**
<font style="color:#000000;">本章包含重要的安全信息，任何个人或者机构在使用设备之前，尤其在第一次通电前，必须阅读并理解这些信息。请务必遵守并执行本手册中的所有组装说明和指南，这一点非常重要。特别地，注意与警告标志相关的文本。在使用设备前，请务必获取并阅读《PIKA用户手册》。有任何相关使用的疑问均可以联系我们support@agilex.ai。</font>

**<font style="color:#000000;">警告标识：</font>****<font style="color:#000000;">⚠</font>**<font style="color:#000000;">这指的是可能引发危险的情况，如果不避免，可导致人员伤害、财产损失和设备严重损坏。 </font>

**<font style="color:#000000;">警告</font>****<font style="color:#000000;">⚠</font>****<font style="color:#000000;">：</font>**<font style="color:#000000;">如果PIKA设备以任何方式被损坏、更改或修改，松灵机器人将不承担任何责任。松灵机器人对由于程序出错导致或操作故障而对设备或任何其他设备造成的任何损坏不承担任何责任。</font>

<font style="color:#000000;">责任限制：一旦开始使用本设备，即视为您已阅读、理解、认可和接受本产品的用户手册、安全信息的全部条款和内容。使用者承诺对自身的行为及因此而产生的所有后果负责。使用者承诺仅出于正当目的使用设备，并且同意本条款及松灵机器人可能制定的任何相关政策或者准则。在使用PIKA设备过程中，请务必严格遵守并执行包括但不限于用户手册和安全信息的要求，对于违反所提示的使用行为或不可抗因素导致的人身伤害、事故、财产损失、法律纠纷、利益冲突，松灵机器人将不承担任何责任。PIKA设备不适合未满 18 周岁及其他不具备完全民事行为能力的人士使用，请避免上述人士接触本产品，在有上述人士出现的场合操作时请格外注意。</font>

<font style="color:#000000;">PIKA设备的集成商和终端客户有责任确保遵循相关规定和切实的法律法规，确保完整的数据采集应用实例中不存在任何重大危险。</font>

<font style="color:#000000;">这包括但不限于以下内容：</font>

**<font style="color:#000000;">有效性和责任         </font>**<font style="color:#000000;">                                                                                 </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">对完整的数据采集系统做一个风险评估。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">将风险评估定义的其他机械的附加安全设备连接在一起。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确认整个数据采集系统包括软件和硬件系统的设计和安装准确无误。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">设备相关功能需要集成商和终端客户遵循相关规定和切实可行的法律法规进行安全评估，确保开发完成的数据采集系统在实际应用中不存在任何重大危险和安全隐患。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">在操作和使用设备之前已经知晓可能存在的安全风险。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确保用户不会对任何安全措施加以修改</font>

**<font style="color:#000000;">环境    </font>**<font style="color:#000000;">                                                                                              </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">首次使用，请先仔细阅读本手册，了解基本操作内容与操作规范。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">选择相对空旷区域使用，PIKA设备本身是不带任何自动避障传感器。</font>

<font style="color:#000000;">●</font><font style="color:#000000;"> </font><font style="color:#000000;">在0℃~40℃的环境温度中使用。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">防水、防尘能力为IP22。</font>

**<font style="color:#000000;">检查   </font>**<font style="color:#000000;">                                                                                               </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确保设备无明显异常。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">使用时确保线束连接正常。</font>

**<font style="color:#000000;">操作    </font>**<font style="color:#000000;">                                                                                              </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">保证操作时周围区域相对空旷。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">在视距内操作。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">当设备出现异常时，请立即停止使用，避免造成二次伤害。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">当设备出现异常时，请联系相关技术人员，请勿擅自处理。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">请根据设备的IP防护等级在满足防护等级要求的环境中使用。</font>

**<font style="color:#000000;">使用警告</font>****<font style="color:#000000;">⚠</font>****<font style="color:#000000;">：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确保PIKA设备和工具/末端执行器始终都正确并稳固地固定在位。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确保PIKA设备有足够的空间来自由活动。 </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确保已按照风险评估中所定义的建立安全措施。 </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">操作时请不要穿宽松的衣服。操作时请确保长头发束在脑后。 </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">如果设备已损坏或有任何异常，请勿使用。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">确保警告人们的头和脸或者其他身体部分保持在正在操作的PIKA设备或即将开始操作的PIKA设备可触及的范围之外。 </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">切勿改动PIKA设备。对PIKA设备的改动有可能造成集成商无法预测的危险。 </font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">不要将PIKA设备一直暴露在永久性磁场。强磁场可损坏设备。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">将不同的机械连接起来可能加重危险或引发新的危险。始终对整个安装进行全面的风险评估。根据风险评估，不同的功能安全等级可能适用；因此当需要不同的安全和紧急停止性能等级时，始终选择最高的性能等级。始终都要阅读和理解安装中使用到的所有设备的手册。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">PIKA设备不适合未满 18 周岁及其他不具备完全民事行为能力的人士使用。</font>

# **<font style="color:#1a1a1a;">一、</font>****<font style="color:#1a1a1a;">产品介绍 Introduction</font>**
## **<font style="color:#1a1a1a;">1.1 </font>****<font style="color:#1a1a1a;">产品概述</font>**
<font style="color:#333333;">Pika 数据套装产品（以下简称Pika）是一款针对</font>**<font style="color:#333333;">具身智能</font>**<font style="color:#333333;">领域数据采集场景的</font>**<font style="color:#333333;">空间数据采集产品</font>**<font style="color:#333333;">，</font><font style="color:#333333;">是一款面向通用操作、轻量化的便携式采执一体化解决方案， 由采集装置及</font><font style="color:#333333;">模型推理执行器</font><font style="color:#333333;">以及配套的定位基站和数据背包</font><font style="color:#333333;">构成。</font><font style="color:#333333;">支持</font><font style="color:#333333;">高效、准确、快捷、轻量的采集机器人的空间操作数据。</font>

<font style="color:#333333;">Pika</font><font style="color:#333333;">具备</font><font style="color:#333333;">超高精度的</font>**<font style="color:#333333;">毫米级空间信息采集能力</font>**<font style="color:#333333;">，</font><font style="color:#333333;">支持</font><font style="color:#333333;">采集</font><font style="color:#333333;">数据</font><font style="color:#333333;">涵盖六自由度精准空间信息、深度信息、超广</font><font style="color:#333333;">角</font><font style="color:#333333;">可见光视觉信息以及夹持信息。满足具身智能</font><font style="color:#333333;">领域</font><font style="color:#333333;">的</font>**<font style="color:#333333;">数据采集多信息融合需求</font>**<font style="color:#333333;">。执行</font><font style="color:#333333;">器</font><font style="color:#333333;">可以基于</font><font style="color:#333333;">采集器（Pika Sense）</font><font style="color:#333333;">采集的数据用于模型推理的执行器终端。</font>

<font style="color:#333333;">Pika由便携式数据采集单元 (Pika Sense)、末端执行器(Pika Gripper)、 定位基站(Pika Station) 、便携式数据背包(Pika Package)组成（如下图所示），Pika Sense和Pika Station可搭配Pika Package或笔记本电脑使用，进行数据采集；Pika Gripper可单独使用进行推理动作；Pika Sense、Pika Station搭配Pika Gripper 及笔记本电脑可进行遥操作数据采集。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442564008-97c9c927-97c0-4b51-b20b-707967f24d51.png" width="529" title="" crop="0,0,1,1" id="ubc0e4b55" class="ne-image">

## **<font style="color:#1a1a1a;">1.2 </font>****<font style="color:#1a1a1a;">产品</font>****<font style="color:#1a1a1a;">特性</font>**
<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">手持终端轻巧：</font>**<font style="color:#333333;">质量轻</font><font style="color:#333333;">巧</font><font style="color:#333333;">，相比于UMI质量</font><font style="color:#333333;">更轻便；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">位姿定位精度高：</font>**<font style="color:#333333;">最高达1.5mm空间精度，无惧墙面/桌面等纹理退化高场景</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">传感器丰富</font>**<font style="color:#333333;">：配置视角近200°鱼眼相机，两手持终端之间可见，对于双臂任务有极大帮助；增</font><font style="color:#000000;">加双目深度相机</font><font style="color:#333333;">，采集高精度的深度数据；配置高精度位置编码器，可采集位置夹持信息</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">配置完整执行器：</font>**<font style="color:#333333;">采集终端和执行器终端的传感器配置一致，便于复现模型算法</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">直接输出位置信息：</font>**<font style="color:#333333;">无需后处理、后同步数据，数据质量高，数据采集更高效</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">交互友好：</font>**<font style="color:#333333;">满足人机交互设计，长时间作业不劳累</font>

## **<font style="color:#1a1a1a;">1.3 </font>****<font style="color:#1a1a1a;">产品参数</font>**
| <font style="color:#333333;">类别</font> | <font style="color:#333333;">项目</font> | | <font style="color:#333333;">参数</font> |
| --- | :---: | --- | --- |
| <font style="color:#333333;">Pika Sense </font> | <font style="color:#333333;">尺寸</font> | | <font style="color:#333333;">长215×宽220×高257mm</font> |
| | <font style="color:#333333;">重量</font> | | <font style="color:#333333;">550g</font> |
| | <font style="color:#333333;">最大夹持力</font> | | <font style="color:#333333;">2KG</font> |
| | <font style="color:#333333;">空间定位精度</font> | | <font style="color:#333333;">±1.5mm</font><font style="color:#333333;">（/</font><font style="color:#333333;">无遮挡情况）</font> |
| | <font style="color:#333333;">定位数据输出频率</font> | | <font style="color:#333333;">120HZ</font> |
| | <font style="color:#333333;">定位标签续航</font> | | <font style="color:#333333;">9h</font> |
| | <font style="color:#333333;">输出数据</font> | | <font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">6D 空间坐标</font><br/><font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">夹爪开合转轴角度</font><br/><font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">深度数据</font><br/><font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">RGB数据</font><br/><font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">IMU数据（早期版本支持）</font> |
| | <font style="color:#333333;">二次开发</font> | | <font style="color:#333333;">ROS1 ROS2 URDF</font> |
| | <font style="color:#333333;">通讯接口</font> | | <font style="color:#333333;">TYPE-C</font> |
| | <font style="color:#333333;">夹爪</font> | <font style="color:#333333;">夹爪类型</font> | <font style="color:#333333;">两指夹爪</font> |
| | | <font style="color:#333333;">最大开合尺寸</font> | <font style="color:#333333;">95mm</font> |
| | | <font style="color:#333333;">最小开合尺寸</font> | <font style="color:#333333;">0（可夹持纸张）</font> |
| | | <font style="color:#333333;">开合转轴旋转精度</font> | <font style="color:#333333;">±0.1°</font> |
| | | <font style="color:#333333;">输出反馈频率</font> | <font style="color:#333333;">100hz</font> |
| | <font style="color:#333333;">惯性传感器</font><br/><font style="color:#333333;">（早期版本支持）</font> | <font style="color:#333333;">类型</font> | <font style="color:#333333;">9轴陀螺仪</font> |
| | | <font style="color:#333333;">陀螺仪零</font><font style="color:#333333;">漂</font><font style="color:#333333;">稳定性</font> | <font style="color:#333333;">2.5°/H</font> |
| | | <font style="color:#333333;">加速度计零漂稳定性</font> | <font style="color:#333333;">30ug</font> |
| | | <font style="color:#333333;">输出反馈频率</font> | <font style="color:#333333;">100hz</font> |
| | <font style="color:#333333;">深度相机</font> | <font style="color:#333333;">深度最优距离</font> | <font style="color:#333333;">7cm - 50cm</font> |
| | | <font style="color:#333333;">曝光方式</font> | <font style="color:#333333;">全局快门</font> |
| | | <font style="color:#333333;">深度测量方式</font> | <font style="color:#333333;">双目视觉</font> |
| | | <font style="color:#333333;">深度FOV</font> | <font style="color:#333333;">87°(水平)×58°(竖直)</font> |
| | | <font style="color:#333333;">最小深度距离</font> | <font style="color:#333333;">7cm @ 480p</font> |
| | | <font style="color:#333333;">最大深度输出分辨率</font> | <font style="color:#333333;">1280×720</font> |
| | | <font style="color:#333333;">深度测量精度</font> | <font style="color:#333333;">±2% at 50cm</font> |
| | | <font style="color:#333333;">深度最大帧率</font> | <font style="color:#333333;">90FPS</font> |
| | | <font style="color:#333333;">RGB输出</font> | <font style="color:#333333;">支持</font> |
| | | <font style="color:#333333;">RGB视场</font> | <font style="color:#333333;">87°(水平)×58°(竖直)</font> |
| | | <font style="color:#333333;">RGB</font><font style="color:#333333;">最大</font><font style="color:#333333;">分辨率</font> | <font style="color:#333333;">1280×720</font> |
| | | <font style="color:#333333;">RGB最大帧率</font> | <font style="color:#333333;">90FPS</font> |
| | <font style="color:#333333;">广角相机</font> | <font style="color:#333333;">视角</font> | <font style="color:#333333;">对角200°</font> |
| | | <font style="color:#333333;">可输出</font><font style="color:#333333;">帧率</font> | <font style="color:#333333;">•1280*720 @ </font><font style="color:#333333;">3</font><font style="color:#333333;">0fps </font><br/><font style="color:#333333;">•640*480 @ </font><font style="color:#333333;">3</font><font style="color:#333333;">0</font><font style="color:#333333;">/60/90</font><font style="color:#333333;">fps </font> |
| <font style="color:#333333;">Pika Gripper</font> | <font style="color:#333333;">尺寸</font> | | <font style="color:#333333;">长215x宽191x高143mm</font> |
| | <font style="color:#333333;">重量</font> | | <font style="color:#333333;">690</font><font style="color:#333333;">g</font> |
| | <font style="color:#333333;">最大加持力</font> | | <font style="color:#333333;">2KG</font> |
| | <font style="color:#333333;">机械接口说明</font> | | <font style="color:#333333;">法兰连接</font> |
| | <font style="color:#333333;">夹爪</font> | <font style="color:#333333;">夹爪类型</font> | <font style="color:#333333;">两指夹爪</font> |
| | | <font style="color:#333333;">最大开合尺寸</font> | <font style="color:#333333;">95mm</font> |
| | | <font style="color:#333333;">最小开合尺寸</font> | <font style="color:#333333;">0（可夹持纸张）</font> |
| | | <font style="color:#333333;">开合测量精度</font> | <font style="color:#333333;">±0.1°</font> |
| | <font style="color:#333333;">惯性传感器</font><br/><font style="color:#333333;">（早期版本支持）</font> | <font style="color:#333333;">类型</font> | <font style="color:#333333;">9轴陀螺仪</font> |
| | | <font style="color:#333333;">陀螺仪零</font><font style="color:#333333;">漂</font><font style="color:#333333;">稳定性</font> | <font style="color:#333333;">2.5°/H</font> |
| | | <font style="color:#333333;">加速度计零漂稳定性</font> | <font style="color:#333333;">30ug</font> |
| | | <font style="color:#333333;">输出反馈频率</font> | <font style="color:#333333;">100hz</font> |
| | <font style="color:#333333;">深度相机</font> | <font style="color:#333333;">深度最优距离</font> | <font style="color:#333333;">7cm - 50cm</font> |
| | | <font style="color:#333333;">曝光方式</font> | <font style="color:#333333;">全局快门</font> |
| | | <font style="color:#333333;">深度测量方式</font> | <font style="color:#333333;">双目视觉</font> |
| | | <font style="color:#333333;">深度FOV</font> | <font style="color:#333333;">87°(水平)×58°(竖直)</font> |
| | | <font style="color:#333333;">最小深度距离</font> | <font style="color:#333333;">7cm @ 480p</font> |
| | | <font style="color:#333333;">最大深度输出分辨率</font> | <font style="color:#333333;">1280×720</font> |
| | | <font style="color:#333333;">深度测量精度</font> | <font style="color:#333333;">±2% at 50cm</font> |
| | | <font style="color:#333333;">深度最大帧率</font> | <font style="color:#333333;">90FPS</font> |
| | | <font style="color:#333333;">RGB输出</font> | <font style="color:#333333;">支持</font> |
| | | <font style="color:#333333;">RGB视场</font> | <font style="color:#333333;">87°(水平)×58°(竖直)</font> |
| | | <font style="color:#333333;">RGB分辨率</font> | <font style="color:#333333;">1280×720</font> |
| | | <font style="color:#333333;">RGB最大帧率</font> | <font style="color:#333333;">90FPS</font> |
| | <font style="color:#333333;">广角相机</font> | <font style="color:#333333;">视角</font> | <font style="color:#333333;">对角200°</font> |
| | | <font style="color:#333333;">可</font><font style="color:#333333;">输出帧率</font> | <font style="color:#333333;">•1280*720 @ 30fps </font><br/><font style="color:#333333;">•640*480 @ 30/60/90fps </font> |
| <font style="color:#333333;">Pika Station</font> | <font style="color:#333333;">基站</font> | <font style="color:#333333;">水平FOV</font> | <font style="color:#333333;">110°</font> |
| | | <font style="color:#333333;">垂直FOV</font> | <font style="color:#333333;">150°</font> |
| | <font style="color:#333333;">基站三脚架</font> | <font style="color:#333333;">最大高度</font> | <font style="color:#333333;">2.1m</font> |
| | | <font style="color:#333333;">俯仰调节</font> | <font style="color:#333333;">支持</font> |
| | <font style="color:#333333;">电池规格</font> | | <font style="color:#333333;">12V@10AH</font> |
| | <font style="color:#333333;">典型功耗</font> | | <font style="color:#333333;">3W</font> |
| | <font style="color:#333333;">续航时间</font> | | <font style="color:#333333;">30H</font> |
| | <font style="color:#333333;">工作电压</font> | | <font style="color:#333333;">12V</font> |
| <font style="color:#333333;">Pika Package</font> | <font style="color:#333333;">便携式数据背包</font><font style="color:#333333;">(选配更新中)</font> | | |


## **<font style="color:#1a1a1a;">1.4 实物展示</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442567355-32e2ff5d-775f-4c0a-906b-1d72f7780d4b.png" width="529" title="" crop="0,0,1,1" id="u1b5aae5c" class="ne-image">

## **<font style="color:#1a1a1a;">1.5 产品清单</font>**
| <font style="color:#333333;">产品</font> | <font style="color:#333333;">型号</font> | <font style="color:#333333;">数量</font> |
| :---: | :---: | :---: |
| <font style="color:#333333;">Pika Station</font> | <font style="color:#333333;">三脚架</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">定位基站</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">电池</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">电源适配器</font> | <font style="color:#333333;">1</font> |
| <font style="color:#333333;">Pika Sense</font> | <font style="color:#333333;">手持终端</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">USB接收端</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">USB转TPYEC数据线</font><font style="color:#333333;">*2m</font> | <font style="color:#333333;">1</font> |
| <font style="color:#333333;">Pika Gripper</font> | <font style="color:#333333;">Gripper终端</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">XT30供电线*0.35m</font> | <font style="color:#333333;">1</font> |
| | <font style="color:#333333;">USB转TPYEC数据线</font><font style="color:#333333;">*2m</font> | <font style="color:#333333;">1</font> |


## **<font style="color:#1a1a1a;">1.5 使用流程</font>**
**<font style="color:#333333;">Pika有</font>****<font style="color:#333333;">三</font>****<font style="color:#333333;">种使用方式：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">单独使用Pika Sense与Pika Station搭配，进行手持式数据采集</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442567408-379a0430-4826-4640-b2ab-8e54dc2acce8.png" width="695" title="" crop="0,0,1,1" id="u173a21f2" class="ne-image">

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">单独使用Pika Gripper进行推理执行（将Gripper作为单独的夹爪进行使用）；</font>

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442567564-99e10f31-5f56-4ff4-a807-409108b72da5.jpeg" width="635" title="" crop="0,0,1,1" id="u25e861c7" class="ne-image">

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">Pika Sense、Pika Station、Piper 两指夹爪结合进行遥操采集（Pika Gripper适配中，或者Pika Sense、Pika Station搭配其他任意臂进行遥操作</font>

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442567664-96a49030-d453-470d-8194-603053f22040.jpeg" width="874" title="" crop="0,0,1,1" id="u8d895a93" class="ne-image">

## **<font style="color:#1a1a1a;">1.6 模块介绍</font>**
<font style="color:#333333;">Pika 完整产品包含了Pika数据采集器（Pika Sense）、Pika执行单元(Pika Gripper)、高精度定位基站(Pika Station)及数据背包（Pika Package）。Pika数据采集器（Pika Sense）包含手持操作器、高精度深度相机、广角单目相机、高精度编码器以及二指夹爪构成。Pika 执行器器包含</font><font style="color:#333333;">两指夹爪、深度相机、广角相机、高精度无刷电机构成。高精度定位基站系统包含移动固定支架以及配套电池，满足在空间中Pika数据单元的毫米级空间定位。</font>

### **<font style="color:#1a1a1a;">1.6.1 数据采集器 Pika Sense</font>**
<font style="color:#333333;">Pika数据采集单元主要用于数据采集，可以手持进行独立的数据采集动作。由手持操作器、高精度深度相机、广角单目相机、高精度编码器以及二指夹爪构成。也可以基于高精度定位数据对机械臂等设备进行遥操作。用于数据的采集。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442567768-15bd4357-aaca-4702-9692-ffdb311b1fe6.png" width="737" title="" crop="0,0,1,1" id="u1337de0e" class="ne-image">

| <font style="color:#333333;">1</font> | <font style="color:#333333;">定位标签</font> | <font style="color:#333333;">8</font> | <font style="color:#333333;">定位标签电源按钮</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">2</font> | <font style="color:#333333;">定位标签充电口</font> | <font style="color:#333333;">9</font> | <font style="color:#333333;">定位标签指示灯</font> |
| <font style="color:#333333;">3</font> | <font style="color:#333333;">超广角相机</font> | <font style="color:#333333;">10</font> | <font style="color:#333333;">TYPE-C接口</font> |
| <font style="color:#333333;">4</font> | <font style="color:#333333;">深度相机</font> | <font style="color:#333333;">11</font> | <font style="color:#333333;">归零按键</font> |
| <font style="color:#333333;">5</font> | <font style="color:#333333;">深度相机</font> | <font style="color:#333333;">12</font> | <font style="color:#333333;">状态指示灯</font> |
| <font style="color:#333333;">6</font> | <font style="color:#333333;">夹爪内层护垫</font> | <font style="color:#333333;">13</font> | <font style="color:#333333;">手持操作器</font> |
| <font style="color:#333333;">7</font> | <font style="color:#333333;">两指夹爪</font> | <font style="color:#333333;">--</font> | <font style="color:#333333;">-</font> |


<font style="color:#333333;">Pika Sense状态指示灯含义说明</font><font style="color:#333333;">（如上图12所示：指Pika Sense 背部的指示灯）</font><font style="color:#333333;">：</font>

| <font style="color:#333333;">颜色</font> | <font style="color:#333333;">状态</font> | <font style="color:#333333;">含义</font> |
| :---: | :---: | :---: |
| <font style="color:#333333;">绿色</font> | <font style="color:#333333;">闪烁</font> | <font style="color:#333333;">上电自检中</font> |
| | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">自检通过进入待机状态（录制功能处于关闭状态）</font> |
| <font style="color:#333333;">蓝色</font> | <font style="color:#333333;">呼吸灯</font> | <font style="color:#333333;">录制功能处于开启状态</font> |
| <font style="color:#333333;">红色</font> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">磁场信号丢失</font> |


:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

+ <font style="color:#333333;">在待机状态下，</font><font style="color:#ff0000;">夹爪快速连续闭合2次可激活录制功能，再次快速闭合两下可回到待机状态</font><font style="color:#333333;">。</font>
+ <font style="color:#333333;">顶部定位标签为内部电池单独供电，需要定时充电，其他模组通过Type-C接口线束供电使用。</font>
+ <font style="color:#333333;">自检完成后，绿色闪烁变更为绿色常亮，此时绿蓝 2 种颜色，作用是提示快速双击这个操作是否成功触发，成功触发一次灯颜色就反转一次。</font>

:::

<font style="color:#333333;">归零按键功能（位置11 背部两个指示灯中间的按键）：</font>

| <font style="color:#333333;">功能</font> | <font style="color:#333333;">操作方式</font> | <font style="color:#333333;">说明</font> |
| :---: | :---: | :---: |
| <font style="color:#333333;">夹爪零位设置</font> | <font style="color:#333333;">双击按键</font> | <font style="color:#333333;">设置夹爪当前位置为零位</font> |


:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#333333;">出厂已设置，非必要不操作（如需操作，请在夹爪完全闭合的状态下执行按键操作）。</font>

:::

<font style="color:#333333;">PIKA Sense上面的定位标签与采集主机（常用的为笔记本或者工控机）之间通过USB进行无线通讯，所以每一个Pika Sense上的定位标签均需要与</font><font style="color:#333333;">无线接收器</font><font style="color:#333333;">进行配对使用。</font><font style="color:#333333;">无线接收器</font><font style="color:#333333;">如下图所示：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442570841-f6b7383b-142d-4a57-bbde-2f30bd2e6f08.png" width="224" title="" crop="0,0,1,1" id="u28a10959" class="ne-image">

<font style="color:#333333;">将USB接收器与定位标签配对成功后</font><font style="color:#333333;">（配对方法参见2.2无线接收器与电脑通过USB线束连接配对）</font><font style="color:#333333;">，将无线接收器插入电脑中，将定位标签长按3秒开机，如定位标签灯由蓝变绿，则代表配对成功。</font>

<font style="color:#333333;">定位标签状态指示灯</font><font style="color:#333333;">含义说明（这里指定位标签上面的指示灯）：</font>

| <font style="color:#333333;">颜色</font> | <font style="color:#333333;">状态</font> | <font style="color:#333333;">含义</font> |
| :---: | :---: | :---: |
| <font style="color:#333333;">绿色</font> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">无线接收器连接成功</font> |
| <font style="color:#333333;">蓝色</font> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">空闲状态，30秒无连接便会自动关闭电源</font> |
| <font style="color:#333333;">蓝色</font> | <font style="color:#333333;">闪烁</font> | <font style="color:#333333;">无线接收器配对中</font><font style="color:#333333;">（适用于初次使用软件配对）</font> |
| <font style="color:#333333;">红色</font> | <font style="color:#333333;">闪烁</font> | <font style="color:#333333;">电量低于10%</font> |
| <font style="color:#333333;">黄色</font> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">充电中</font> |
| <font style="color:#333333;">白色</font> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">满电</font> |


### **<font style="color:#1a1a1a;">1.6.2 数据执行器 Pika Gripper </font>**
<font style="color:#000000;">Pika 执行器</font><font style="color:#000000;">（以下简称执行器）</font><font style="color:#000000;">单元包含两指夹爪、深度相机、广角相机构成。</font><font style="color:#000000;">执行器配置有标准的固定结构，同时可以选配不同的安装法兰</font><font style="color:#000000;">（此法兰为选配配件，需要单独联系我们进行采购）</font><font style="color:#000000;">，用于固定在不同的机械臂上，例如松灵机器人的Piper六自由度机械臂上，或其他的第三方机械臂。其包含一个执行器电机电源供电接口，以及</font><font style="color:#000000;">一个Type-C用于和各</font><font style="color:#000000;">传感器的通讯接口。</font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442573973-124d78f4-f623-48ed-bde5-a951e3f057f9.png" width="604" title="" crop="0,0,1,1" id="ue2f4a2b4" class="ne-image">

| <font style="color:#333333;">1</font> | <font style="color:#333333;">广角相机</font> | <font style="color:#333333;">7</font> | <font style="color:#333333;">供电通信接口</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">2</font> | <font style="color:#333333;">深度相机</font> | <font style="color:#333333;">8</font> | <font style="color:#333333;">归零按钮</font> |
| <font style="color:#333333;">3</font> | <font style="color:#333333;">深度相机</font> | <font style="color:#333333;">9</font> | <font style="color:#333333;">状态指示灯</font> |
| <font style="color:#333333;">4</font> | <font style="color:#333333;">夹爪移动滑轨</font> | <font style="color:#333333;">10</font> | <font style="color:#333333;">TPYE-C数据通信接口</font> |
| <font style="color:#333333;">5</font> | <font style="color:#333333;">夹爪内层护垫</font> | <font style="color:#333333;">11</font> | <font style="color:#333333;">法兰安装位置</font> |
| <font style="color:#333333;">6</font> | <font style="color:#333333;">两指夹爪</font> | <font style="color:#333333;">--</font> | |


<font style="color:#333333;">Pika Gripper状态指示灯含义说明：</font>

| <font style="color:#333333;">颜色</font> | <font style="color:#333333;">颜色示意图</font> | <font style="color:#333333;">状态</font> | <font style="color:#333333;">含义</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">绿色 </font> | <img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442575220-40e54c3b-9d09-4b52-ad07-e824fe597acc.png" width="60" title="" crop="0,0,1,1" id="u29d7ffde" class="ne-image"> | <font style="color:#333333;">闪烁</font> | <font style="color:#333333;">上电自检中</font> |
| | | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">自检通过进入待机状态（夹爪处于失能状态）</font> |
| <font style="color:#333333;">蓝色</font> | <img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442575971-8143109e-c8c7-436f-9f9a-9fac0acc0f45.png" width="62" title="" crop="0,0,1,1" id="u56963fab" class="ne-image"> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">进入工作状态（夹爪处于使能状态）</font> |
| <font style="color:#333333;">红色</font> | <img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442577356-669d4600-3e8e-4c01-b92c-8cf5f6a79996.png" width="67" title="" crop="0,0,1,1" id="uf4e58317" class="ne-image"> | <font style="color:#333333;">常亮</font> | <font style="color:#333333;">夹爪电机故障警告（具体故障需通过故障检测数据帧判定）</font> |


<font style="color:#333333;">Pika Grippe</font><font style="color:#333333;">r</font><font style="color:#333333;"> 按键功能说明：</font>

| <font style="color:#333333;">功能</font> | <font style="color:#333333;">操作方式</font> | <font style="color:#333333;">说明</font> |
| :---: | :---: | :---: |
| <font style="color:#333333;">夹爪零位设置</font> | <font style="color:#333333;">双击按键</font> | <font style="color:#333333;">设置夹爪当前位置为零位</font> |


:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#333333;">出厂已设置，非必要不操作（如需操作，请在夹爪完全闭合的状态下执行按键操作）。</font>

:::

<font style="color:#333333;">Pika-Gripper供电通信接口说明：</font>

<font style="color:#333333;">供电接口类型为XT30(PB)，其中复用的通讯口（CAN口）未使用，通讯和控制接口统一使用Type-c接口进行通讯，使用时，使用一个</font>**<font style="color:#333333;">USB3.0</font>**<font style="color:#333333;">含以上的线束</font><font style="color:#333333;">与夹爪相连接即可。电源接口以及接口定义如下表:</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442577770-fd966187-4d16-4f1d-881f-a575e9ffba5d.png" width="250" title="" crop="0,0,1,1" id="u36868ba8" class="ne-image">

| <font style="color:#333333;">1</font> | <font style="color:#333333;">24V供电</font><font style="color:#333333;"> -</font> | <font style="color:#333333;">4</font> | <font style="color:#333333;">CAN-H（预留）</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">2</font> | <font style="color:#333333;">24V供</font><font style="color:#333333;">电 +</font> | <font style="color:#333333;">5</font> | <font style="color:#333333;">TPYE-C</font> |
| <font style="color:#333333;">3</font> | <font style="color:#333333;">CAN-L（预留）</font> | <font style="color:#333333;">---</font> | <font style="color:#333333;">---</font> |


### **<font style="color:#1a1a1a;">1.6.3 定位基站 Pika Station</font>**
<font style="color:#333333;">高精度定位基站系统包含移动固定支架以及配套电池，满足在空间中Pika数据单元的毫米级空间定位。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442577823-78bec7d6-c519-4999-b8ad-9e2101b9779b.png" width="604" title="" crop="0,0,1,1" id="u7d97eebc" class="ne-image">

| <font style="color:#000000;">1</font> | <font style="color:#000000;">状态指示灯</font> | <font style="color:#000000;">6</font> | <font style="color:#000000;">基站三脚架</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#000000;">2</font> | <font style="color:#000000;">前面板</font> | <font style="color:#000000;">7</font> | <font style="color:#000000;">定位基站</font> |
| <font style="color:#000000;">3</font> | <font style="color:#000000;">电源端口</font> | <font style="color:#000000;">8</font> | <font style="color:#000000;">电池</font><font style="color:#000000;">（最新版本电池请安装在下部支架位置）</font> |
| <font style="color:#000000;">4</font> | <font style="color:#000000;">螺纹安装孔</font> | <font style="color:#000000;">9</font> | <font style="color:#000000;">频道设置孔</font> |
| <font style="color:#000000;">5</font> | <font style="color:#000000;">Micro-USB口</font> | <font style="color:#000000;">---</font> | <font style="color:#000000;">---</font> |


**定位基站供电说明：**  
定位基站配备两种充电器，支持两种供电方式：

**方式一：**通过配套的 HTC 交互式电源供应器直接给基站供电（220V 交流输入）

使用如下图适配器：

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749794319458-b6cd0644-664d-45b2-beba-ee1428db709d.png" width="428.4000244140625" title="" crop="0,0,1,1" id="ua21f12b6" class="ne-image">

    基站供电线束

**方式二 : **通过配套电池给基站供电（使用如下线束连接电池与基站，电池使用对应下图充电器充电）

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749797921284-fef5b1f9-2715-46ba-906c-800b41686980.png" width="336.4000244140625" title="" crop="0,0,1,1" id="u4e3df909" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749797911086-b22d9215-0a27-40dd-9f99-2d265d9fdbd3.png" width="334.4000244140625" title="" crop="0,0,1,1" id="u7b849978" class="ne-image">

                        电池-基站连接线                                                                电池充电线

### **<font style="color:#1a1a1a;">1.6.4 数据背包 Pika Package（选配）</font>**
:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#333333;">Pika Package 属于选配配件，默认不提供，如如果可以联系我们销售或者相关人员进行采购。</font>

:::

<font style="color:#333333;">数据背包包含了一个数据记录工控机以及其工作所需要的电池，以及固定背带构成，通过内置的软件和算法可以实现数据</font><font style="color:#333333;">采集器（Pika Sense）</font><font style="color:#333333;">的数据采集与存储以及数据导出。数据记录工控机最大支持两个数据</font><font style="color:#333333;">采集器（Pika Sense）</font><font style="color:#333333;">同时工作。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442578025-daee73c0-ce25-4b64-bc84-517394e06df0.png" width="295" title="" crop="0,0,1,1" id="u0a29cd79" class="ne-image">

| <font style="color:#333333;">1</font> | <font style="color:#333333;">固定背带</font> | <font style="color:#333333;">2</font> | <font style="color:#333333;">数据记录工控机</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">3</font> | <font style="color:#333333;">电池</font> | <font style="color:#333333;">---</font> | <font style="color:#333333;">---</font> |


# **<font style="color:#1a1a1a;">二、</font>****<font style="color:#1a1a1a;"> </font>****<font style="color:#1a1a1a;">基站与</font>****<font style="color:#1a1a1a;">pika配置</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442579045-02edb87e-4b5b-4c90-b63c-acb87972070b.png" width="604" title="" crop="0,0,1,1" id="u4bd9828e" class="ne-image">

<font style="color:#333333;">如上图所示，为Pika Station+Pika Sense 数采整体使用流程，</font><font style="color:#333333;">在正式进行数据采集作业之前，需要先进行基站的安装与部署调试，然后进行基站的配对校准，最后开启采集器（Pika Sense）（初次使用采集器需要采集器与接收器进行软件适配），进行数据采集。	</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">设置基站</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">校准基站</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">连接电脑</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">启动采集</font>

## **<font style="color:#1a1a1a;">2.1 基站部署</font>**
<font style="color:#333333;">基站的部署会影响到定位器的定位，在数据采集之前第一步先进行基站的部署与测试。</font>

#### **<font style="color:#1a1a1a;">2.1.1 基站视角</font>**
**<font style="color:#555555;background-color:#ffffff;">基站视角</font>****<font style="color:#333333;">：</font>**<font style="color:#333333;">基站的水平视场为 150 度，垂直视场为 110 度。为了最大限度地扩大操作区，请将基站安装在高于头部的位置（距地面的距离最好大于 2 米 或 6.5 英尺），并将各基站的角度调整为 25 度到 35 度之间。（视角如下图所示）</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442579423-0c41cba7-6ef4-400e-9d43-ee6393861dd6.png" width="276" title="" crop="0,0,1,1" id="u5cdc8808" class="ne-image">

#### **<font style="color:#1a1a1a;">2.1.2 基站覆盖范围：</font>**
**<font style="color:#333333;">两个基站：</font>**<font style="color:#333333;">所需的最小操作区域为 2 米 x 1.5 米（6 英尺 6 英寸 x 5 英尺），最大可达 5 米 x 5 米（16 英尺 5 英寸 x 16 英尺 5 英寸）</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442579421-3c5ddee1-c6ee-4dec-bf90-59277759d7fd.png" width="582" title="" crop="0,0,1,1" id="u6e6da459" class="ne-image">

<font style="color:#333333;">两个基站：单人操作</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#333333;">尽量避免对角摆放，可以呈90°或者同向摆放。</font>

:::

**<font style="color:#333333;">四个基站：</font>**<font style="color:#333333;">四个基站支持的最大覆盖区域为 10 米 x 10 米（32 英尺 10 英寸 x 32 英尺 10 英寸）。（一个场景内最多可使用4个基站）</font>

<font style="color:#333333;">单人操作：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442579471-18f28d83-3030-4629-8149-df1767f85259.png" width="500" title="" crop="0,0,1,1" id="u4a99e606" class="ne-image">

<font style="color:#333333;">双人操作：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442579543-b41bf8e2-5bfc-4bc0-9f6c-5684461b5544.png" width="359" title="" crop="0,0,1,1" id="u43ef82c3" class="ne-image">

**<font style="color:#333333;">三个基站：</font>**<font style="color:#333333;">如果环境为非规则区域，仍旧需要布置3个以上基站，可以参照下图</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580031-c99c7c60-0d3b-48d4-b9b8-7660eb7d2208.png" width="383" title="" crop="0,0,1,1" id="u6e35ee29" class="ne-image">

#### **<font style="color:#1a1a1a;">2.1.3 安装步骤</font>**
<font style="color:#333333;">1.</font><font style="color:#333333;"> </font><font style="color:#333333;">将基站进行安装，推荐将基站安装在房间内的90度视角位置，可以直接固定在墙面。如果空间不允许进行此类安装，也可以将基站安装到三脚架上，或者将基站安放在桌面等稳定的表面上。避免使用不牢固的安装方式或安装在容易振动的表面。</font>

<font style="color:#333333;">2.</font><font style="color:#333333;"> </font><font style="color:#333333;">调整基站角度，使其前面板朝向采集区的中心。每个基站设为最低高度 0.5 米（1.6 英尺）。根据设置的高度，需要向上或向下调整基站角度，以完全覆盖操作区。固定好两个定位基站，保证示教器的活动范围在两个基站的视场内。为获得最佳性能，采集器（Pika Sense）距离基站至少应为 0.5 米（1.6 英尺）。</font>

<font style="color:#333333;">3.</font><font style="color:#333333;"> </font><font style="color:#333333;">为每个基站接上电源线，然后分别插入电源插座或者接通三脚架携带电池以开启电源。</font>

<font style="color:#333333;">4.</font><font style="color:#333333;"> </font><font style="color:#333333;">第一次使用定位基站，需要手动设定定位基站的频道。使用尖锐物体戳基站背后的按钮（如下图9号位置），按1次频道加1，范围从</font><font style="color:#333333;">0</font><font style="color:#333333;">-</font><font style="color:#333333;">15</font><font style="color:#333333;">，</font><font style="color:#333333;">每加一次频道，基站的绿灯则会闪烁一次，使</font><font style="color:#333333;">基站处于不同的频道即可</font><font style="color:#333333;">，同一场景内的基站都需要设置为不同的频道。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580121-05919467-3ae7-4c42-a8dd-a0984f8c1bde.png" width="604" title="" crop="0,0,1,1" id="u6a2a0187" class="ne-image">

<font style="color:#333333;">5.</font><font style="color:#333333;"> </font><font style="color:#333333;">一切准备就绪后，定位基站LED绿色常亮，代表运行正常。</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">安装注意：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#555555;">请勿让任何物体遮住基站前面板。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#555555;">阳光中的红外光会影响基站数据的收发，请在室内无阳光照射的环境下使用。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#555555;">请确保基站安装在采集区外部且已安装牢固，以免意外撞到、掉落或碰撞造成损坏或性能下降。</font>

<font style="color:#555555;">●</font><font style="color:#555555;"> </font><font style="color:#555555;">请勿安装在强照明区域，光照过曝会对基站的性能产生负面影响。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#555555;">在安装好基站后，请记得撕掉前面板上的保护膜。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#555555;">基站开启后，可能会影响附近的某些红外感应器，例如电视红外遥控器使用的感应器。</font>

<font style="color:#555555;">●</font><font style="color:#555555;"> </font><font style="color:#555555;">为实现准确定位，请确保任意基站与</font><font style="color:#555555;">采集器（Pika Sense）</font><font style="color:#555555;">之间的距离在 7 米（23 英尺）范围内。应确保放置基站的位置不存在物理障碍物（比如突出的架子），以便完全覆盖</font><font style="color:#555555;">采集器（Pika Sense）</font><font style="color:#555555;">视场，并确保信号不受阻挡。</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580100-93999794-c111-4df3-b100-353074792ef6.png" width="237" title="" crop="0,0,1,1" id="u45508853" class="ne-image">

#### **<font style="color:#1a1a1a;">2.1.4 同一空间多套设备基站安装</font>**
<font style="color:#333333;">在同一空间内需要部署多套基站搭配采集器使用时，推荐如下方法：</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">优先采用物理隔绝方式，采用隔板等物体将每一套采集设备（基站+采集器）隔开；注意隔板高度要高于基站高度</font><font style="color:#333333;">，参照下图所示‘</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580027-bfcc9e0b-953b-4220-b907-dfc2757eb781.png" width="604" title="" crop="0,0,1,1" id="ue10b4e3a" class="ne-image">

## **<font style="color:#1a1a1a;">2.2 配对采集器（Pika Sense）定位标签</font>****<font style="color:#1a1a1a;">与无线接收器</font>**
:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：  
</font>**<font style="color:#c00000;">● </font>**<font style="color:#000000;">此操作</font>****<font style="color:#ff0000;">必须在Windows系统中完整进行</font>****<font style="color:#000000;">，仅需要一次性设置，如果定位标签没有解绑与更换接收器，无需重复操作，仅需要操作一次；</font>**

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font>**<font style="color:#000000;">后续使用在Ubuntu中</font>****<font style="color:#000000;">直接插入电脑使用即可，</font>****<font style="color:#000000;">无需再次绑定操作。</font>**

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font>**<font style="color:#000000;">如使用有线连接定位标签与电脑，则无需做无线接收器配对。</font>**

:::

<font style="color:#333333;">第一次使用采集器（Pika Sense）</font><font style="color:#333333;">定位标签</font><font style="color:#333333;">，需要将其与无线接收器配对。</font>

<font style="color:#333333;">在进行配对前，需对无线接收器与电脑通过USB线束连接。</font>

<font style="color:#333333;">步骤如下：</font>

<font style="color:#333333;">1、Pika Sense 定位标签开机（长按开机），如Pika Sense 定位标签请先对标签充电（顶部Tpye-C接口为充电口）</font>

<font style="color:#333333;">2、将 USB Type-C 数据线的一端连接到接收器底座，然后将无线信号接收器插入底座。</font>

<font style="color:#333333;">3、将 USB Type-C 数据线的另一端连接到电脑上的 USB 端口。无线信号接收器与电脑的距离至少应有 45 厘米（18 英寸），并且应放在不会移动的位置，具体连接如下图所示。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580132-ebdd8425-029c-460e-8053-08e2a3329dd6.png" width="388" title="" crop="0,0,1,1" id="u2248fb2b" class="ne-image">

<font style="color:#333333;">4、完成连接后开始进行配对：先要安装STEAM软件，完成用户注册。</font>

<font style="color:#333333;">5、</font><font style="color:#333333;">在 Windows 系统上，打开 SteamVR 应用程序。</font>

<font style="color:#333333;">6、单击</font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580806-a93c656e-eeca-4a34-9eab-1f66a2568b7f.png" width="25" title="" crop="0,0,1,1" id="u729b72db" class="ne-image"><font style="color:#333333;"> > 设备 > 配对控制器。</font>

<font style="color:#333333;">7、</font><font style="color:#333333;">在选择您的控制器类型一项中选择HTC Vive 追踪器。</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font>**<font style="color:#000000;"> 如果未在控制器配对窗口中看到</font>****<font style="color:#000000;"> VIVE 追踪器 (3.0)，</font>****<font style="color:#000000;">请单击我要配对其他类型的控制器 ></font>****<font style="color:#000000;"> HTC Vive 追踪器；</font>**

:::

<font style="color:#333333;">8、</font><font style="color:#333333;">长按电源按钮2秒开启定位标签，此时定位标签显示常亮蓝灯，再次</font><font style="color:#333333;">按住电源按钮约 2 秒钟</font><font style="color:#333333;">，</font><font style="color:#333333;">状态指示灯将闪烁蓝色。</font>

<font style="color:#333333;">9、</font><font style="color:#333333;">等待状态指示灯变为绿色。这表示配对已成功。</font>

<font style="color:#333333;">10、在</font><font style="color:#333333;">控制器配对窗口中，单击完成。</font>

<font style="color:#333333;">操作图示如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580903-10199278-833f-4669-ac3d-0b536b075d6d.png" width="604" title="" crop="0,0,1,1" id="ub28cc0fe" class="ne-image">

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

**<font style="color:#000000;">无线连接器与追踪器是一对一，不可一对多。</font>**

:::

<font style="color:#333333;">配对完成之后可以连接器直接接电脑，无需再使用</font><font style="color:#333333;">接收器底座。</font>

## **<font style="color:#1a1a1a;">2.3 电脑连接</font>**
<font style="color:#333333;">若自行准备电脑与采集器（Pika Sense）相连接，其电脑软/硬件需求如下：</font>

| <font style="color:#333333;">软/硬件要求</font> | <font style="color:#333333;">参考参数</font> |
| :---: | :---: |
| <font style="color:#333333;">PC 芯片架构</font> | <font style="color:#333333;">i5-9代及以上</font> |
| <font style="color:#333333;">PC 存储空间</font> | <font style="color:#333333;">1TB以上</font> |
| <font style="color:#333333;">PC 接口</font> | <font style="color:#333333;">USB3.0 x 3</font><font style="color:#333333;">（不可使用拓展坞）</font> |
| <font style="color:#333333;">操作系统</font> | <font style="color:#333333;">Ubuntu22.04</font> |
| <font style="color:#333333;">ROS 版本</font> | <font style="color:#333333;">ROS2-humble</font> |


**<font style="color:#333333;">至此，完成了硬件的所有安装与准备工作，可以开始准备软件部分。</font>**

## **<font style="color:#1a1a1a;">2.4 软件环境部署准备</font>**
<font style="color:#DF2A3F;">(ubuntu22.04-ROS2):</font>

<font style="color:#333333;">1、安装ROS2-humble</font>

<font style="color:#333333;">推荐使</font><font style="color:#333333;">用</font><font style="color:#333333;">fishros</font><font style="color:#333333;">按照提示安装</font>

```plain
cd ~ && wget http://fishros.com/install -O fishros && . fishros
```

<font style="color:#333333;">2、</font><font style="color:#333333;"> </font><font style="color:#333333;">克隆代码</font>

```plain
git clone https://github.com/agilexrobotics/pika_ros.git

cd pika_ros && git checkout ros2

git submodule update --init --recursive

cd ~/pika_ros/src/PikaAnyArm/agx_arm

git clone https://github.com/agilexrobotics/agx_arm_ros.git

cd agx_arm_ros/src/agx_arm_description

git clone -b flattened https://github.com/agilexrobotics/agx_arm_urdf.git

```

<font style="color:#333333;">3、安装依赖</font>

```plain
sudo apt-get update && sudo apt install libjsoncpp-dev libpcap-dev python3-pcl build-essential zlib1g-dev libx11-dev libusb-1.0-0-dev freeglut3-dev liblapacke-dev libopenblas-dev libatlas-base-dev cmake  git libssl-dev  pkg-config libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev g++  python3-pip  libopenvr-dev ros-humble-diagnostic-updater cutecom 
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y && sudo apt update && sudo apt install -y gcc-13 g++-13 libstdc++6 libcurl4-openssl-dev
git clone https://github.com/agilexrobotics/pyAgxArm.git
cd pyAgxArm
pip3 install .
pip3 install "numpy<2"
pip3 install opencv-python
```

<font style="color:#333333;">4、配置USB规则</font>

<font style="color:#333333;">在pika_ros路径下执行：</font>

```plain
cd ~/pika_ros
sudo cp scripts/81-vive.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```

<font style="color:#333333;">执行完这步后，如电脑上插有无线接收器请将其拔插一遍。</font>

<font style="color:#333333;">5、安装Realsense-sdk</font>

<font style="color:#333333;">进入pika_ros/source，将librealsense-2.55.1.zip以及curl-7.75.0.tar.gz解压</font><font style="color:#DF2A3F;">（请勿解压到 pika_ros 目录下的文件夹中，可以解压至 home 目录下）</font><font style="color:#333333;">，修改 librealsense-2.55.1/CMake/external_libcurl.cmake 文件中的 /home/agilex/pika_ros/source/curl-7.75.0 ，将其路径修改成自己 curl-7.75.0 下的路径。</font>

<font style="color:#333333;">运行</font>

```plain
cd librealsense-2.55.1 
mkdir build && cd build && cmake .. && sudo make install
```

<font style="color:#333333;">安装完毕后新建一个终端，输入：</font>

```plain
realsense-viewer
```

<font style="color:#333333;">验证sdk安装</font>

<font style="color:#333333;">将source目录下的install.zip 解压至~/pika_ros 目录下。</font>

<font style="color:#333333;">给install目录加执行权限：</font>

```plain
chmod 777 -R install/
```

<font style="color:#333333;">6、添加环境变量</font>

```plain
echo 'source ~/pika_ros/install/setup.bash' >> ~/.bashrc
```

<font style="color:#333333;">7、编译 pika_ros（需退出 conda 环境再进行编译）</font>

```plain
colcon build
```

<font style="color:#333333;">编译成功后， pika_ros文件层级结构如下：</font>

```plain
├── img
├── install
├── README.md
├── scripts
├── source
├── build
├── log
└── src
```

**<font style="color:#333333;">至此，软件代码配置完毕。</font>**

## **<font style="color:#1a1a1a;">2.5 定位基站校准</font>**
<font style="color:#333333;">使用定位基站对定位标签进行校准的目的是为了获取定位标签在三维空间的绝对坐标值。</font>

<font style="color:#333333;">定位基站通过发射接收红外光来进行校准。</font>

<font style="color:#333333;">开始校准前请确保：</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">打开定位标签并将定位标签放置在基站的FOV范围内且保持静止不动。</font>

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">确保基站和定位标签的灯都是绿色。</font>

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">确保基站的膜撕掉且基站前面无任何遮挡。</font>

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">基站位于</font>**<font style="color:#ff0000;">不同的频道</font>**<font style="color:#000000;">。</font>

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">确保当前所在房间无太阳照射，基站也会影响到其他红外设备的使用。</font>

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">若是第一次部署定位基站，或者定位基站发生了移动，或者定位效果不好，或者切换了频道，都应该进行校准，运行下列指令对定位标签进行校准。</font>

<font style="color:#c00000;">●</font><font style="color:#c00000;"> </font><font style="color:#000000;">校准完不会自动关闭程序，应手动（按Ctrl + C）将程序关掉。</font>

:::

<font style="color:#333333;">校准分以下几种情况，需要根据情况来运行不同的指令：</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

<font style="color:#333333;">1、若是在你的电脑上首次进行基站的校准，运行：</font>

```plain
cd ~/pika_ros/install/pika_locator/lib && ./survive-cli --force-calibrate
```

<font style="color:#333333;">2、若是新增或减少了基站数量，运行：</font>

```plain
cd ~/pika_ros/install/pika_locator/lib && ./survive-cli --force-calibrate
```

<font style="color:#333333;">3、若是进行了频道切换，运行：</font>

```plain
cd ~/pika_ros/install/pika_locator/lib && ./survive-cli --force-calibrate
```

<font style="color:#333333;">4、若是定位飘，或者是在使用过程中移动了基站，则运行</font>

```plain
cd ~/pika_ros/install/pika_locator/lib && ./survive-cli
```

<font style="color:#333333;">以下是第一次使用一个sense进行校准成功后终端输出的信息：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442580816-5f59ecd8-7519-4e7a-bb49-5d8a6042926a.png" width="602" title="" crop="0,0,1,1" id="ub3701cd6" class="ne-image">

<font style="color:#333333;">①：添加了频道2、6的基站</font>

<font style="color:#333333;">②：首次校准会出现该字样，说明2、6频道的基站已被找到并添加</font>

<font style="color:#333333;">③：电脑收到频道2、6基站的数据包</font>

<font style="color:#333333;">④：显示了定位标签的误差（单位/米），看到终端输出该信息，就可以将校准程序关掉了，这里使用Ctrl+C就能将其关闭</font>

<font style="color:#333333;">⑤：Ctrl+C 关闭校准程序时会出现的信息，error failures为0代表无丢包，校准成功，如不为0，则需要检查基站的摆放位置以及当前的环境（如太阳光直射）、电脑的USB口是否对校准有影响，排除掉后再次进行校准，直到error failures为0为止。</font>

<font style="color:#333333;">当按下 Ctrl+C终止程序后出现了报红错误：</font>

```plain
Warning: Libusb poll failed. -10 (LIBUSB_ERROR_INTERRUPTED)
```

<font style="color:#333333;">无需理会，不影响后面的定位。</font>

<font style="color:#333333;">如果使用两个sense进行校准时，终端显示与上面不同的是，会出现：</font>

```plain
Info: MPFIT stats for WM0:
Info: 	seed runs         1 / 11730
Info: 	error failures    0
Info: MPFIT stats for WM1:
Info: 	seed runs         2 / 10790
Info: 	error failures    0
```

<font style="color:#333333;">区别就是多了个 </font><font style="color:#000000;">WM1，代表目前有2个定位标签进行了校准。</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#c00000;">常见校准异常处理</font>**<font style="color:#c00000;"></font>

**<font style="color:#333333;">1.</font>****<font style="color:#333333;"> </font>****<font style="color:#333333;">在执行校准指令过程中，无法找到driver_openvr.so文件</font>**

<font style="color:#333333;">安装依赖： </font><font style="color:#333333;">sudo apt install libopenvr-dev 后再次进行校准</font>

**<font style="color:#333333;">2.</font>****<font style="color:#333333;"> </font>****<font style="color:#333333;">校准时终端一直停留不动，并且没有显示定位误差</font>**

<font style="color:#333333;">	</font><font style="color:#333333;">rm ~/.config/libsurvive/config.json </font>

<font style="color:#333333;">	将</font><font style="color:#333333;">config.json 文件移除后再次进行校准</font>

**<font style="color:#333333;">3.</font>****<font style="color:#333333;"> </font>****<font style="color:#333333;">校准结束后显示有 error failures</font>**

<font style="color:#333333;">	</font><font style="color:#333333;">有 error failures 代表此次校准是失败的，检查当前环境是否有阳光照射或者当下环境 是否有主动发射红外光的设备。再次检查基站摆放位置，确保sense在基站的FOV内。当以上事项都检查完毕，再次运行校准程序。</font>

**<font style="color:#333333;">4.</font>****<font style="color:#333333;"> </font>****<font style="color:#333333;">当校准完成，使用一段时间后发现TF坐标飘了</font>**

<font style="color:#333333;">检查当前环境是否有阳光照射或者当下环境是否有主动发射红外光的设备。再次检查基站摆放位置，确保sense在基站的FOV内。当以上事项都检查完毕，再次运行校准程序。</font>

:::

## **<font style="color:#1a1a1a;">2.6 绑定设备</font>**
:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

**<font style="color:#ff0000;">请不要使用usb-hub！</font>****<font style="color:#000000;">若使用单夹持sense或者单夹爪gripper，则无需设置，可以跳过此项，直接进行到第三节数据采集、第五节gripper使用或者第六节遥操作。若使用双夹持器，则需要进行配置。配置后若更换USB端口，则需重新配置。</font>****<font style="color:#ff0000;">（注意：所要绑定的所有设备需要处于不同的USB端口，更换USB端口需要重新绑定。1个sense和1个gripper同时使用也需要绑定。）</font>**

:::

<font style="color:#333333;">当要使用两个以上的 Pika 时，需要设置pika为sense或者gripper，同时设置左右手，否则无法正确接收数据。</font>

<font style="color:#333333;">首先，打开终端，执行：</font>

```bash
conda deactivate  #退出虚拟环境
```

```plain
cd ~/pika_ros/scripts/
python3 setup_device.py
```

<font style="color:#333333;">1.按照提示选择要绑定的设备</font>

+ <font style="color:#262626;">若2个sense和2个gripper同时使用，请先绑定2个sense后再绑定2个gripper</font>
+ <font style="color:#262626;">helmet 还提供 2 种方式选择，根据情况自行选择是否带定位器</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/12455065/1779346048808-ed79cb6a-df51-48a5-b6f2-31a30d2f12ef.png" width="367.27271931230547" title="" crop="0,0,1,1" id="u3ca13f6c" class="ne-image">

<font style="color:#333333;">2.按照提示插入第一个设备</font><font style="color:#262626;">（注意：所要绑定的所有设备需要处于不同的USB端口）</font>

<font style="color:#333333;">3.选择鱼眼摄像头设备，找到鱼眼摄像头画面并按下s，非鱼眼摄像头则按下q</font><font style="color:#262626;">（注意：需要在摄像头窗口下按下按键）  
</font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442581368-8573bf29-8bed-4a6f-868f-41224bb10846.png" width="604" title="" crop="0,0,1,1" id="u92e87580" class="ne-image">

<font style="color:#333333;">4.按照提示拔出第一个设备，插入第二个设备</font><font style="color:#262626;">（注意：所要绑定的所有设备需要处于不同的USB端口）</font><img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442581534-d3756960-46f8-413a-9563-fea048ec37f8.png" width="604" title="" crop="0,0,1,1" id="ub2195a4a" class="ne-image">

<font style="color:#333333;">5.按照提示完成相同步骤，完成绑定。</font>

:::warning
<font style="color:#ff0000;">错误提示及其处理方法</font>

:::

| <font style="color:#262626;">无法读取到深度摄像头数据</font> | <font style="color:#262626;">1.确保USB已经连接 2.拔插USB设备 3.不使用usb-hub</font> |
| :--- | :--- |
| <font style="color:#262626;">无法读取到串口数据</font> | <font style="color:#262626;">1.确保USB已经连接 2.拔插USB设备 3.不使用usb-hub</font> |
| <font style="color:#262626;">无法读取到鱼眼摄像头数据</font> | <font style="color:#262626;">1.确保USB已经连接 2.拔插USB设备 3.不使用usb-hub</font> |
| <font style="color:#262626;">无法获取设备信息，检查设备连接</font> | <font style="color:#262626;">1.确保USB已经连接 2.拔插USB设备 3.不使用usb-hub</font> |
| <font style="color:#262626;">确保工控机只插入一个USB设备</font> | <font style="color:#262626;">拔插其它设备，只保留pika设备连接</font> |


## **<font style="color:#1a1a1a;">2.7 设置左右手定位器</font>**
<font style="color:#333333;">1、</font><font style="color:#333333;"> </font><font style="color:#333333;">首先完成定位基站的校准。</font>

<font style="color:#333333;">2、然后，运行程序获取左右定位标签的序列号，使用序列号来区分左右手。</font>

<font style="color:#333333;"> </font><font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font><font style="color:#333333;"></font>

```plain
ros2 launch pika_locator get_code.launch.py
```

<font style="color:#333333;">3、一切顺利的话，会在 rviz 中看到除了基座标系（base_link）外，还有两个坐标系。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442581820-99a22836-5e76-40bd-ab37-fd04f3a18a97.png" width="504" title="" crop="0,0,1,1" id="uf824b76e" class="ne-image">

<font style="color:#333333;">此时移动 pika，并记录下你想设置左右手的坐标系名称，例如：LHR-EB902458 设置为左手，LHR-FE98B2BE 设置为右手。随后运行下列指令将左右手的配置写入环境变量里面：</font>

```plain
echo 'export pika_L_code=LHR-EB902458' >> ~/.bashrc
echo 'export pika_R_code=LHR-FE98B2BE' >> ~/.bashrc
source ~/.bashrc
```

<font style="color:#333333;">如果 .bashrc 文件已经存在 pika_L_code、pika_R_code，只需将值修改即可。</font>

<font style="color:#333333;">4、运行设置好左右手程序，打开rviz，手持左右sense运动查看绑定是否正确</font>

<font style="color:#DF2A3F;">启动定位程序(ubuntu22.04-ROS2)</font>

```plain
ros2 launch pika_locator pika_double_locator.launch.py
```

**<font style="color:#333333;">至此，完成了</font>****<font style="color:#333333;">pika设备</font>****<font style="color:#333333;">的所有准备工作。</font>**

## **<font style="color:#1a1a1a;">2.8 开启设备</font>**
**<font style="color:#333333;">可以通过以下命令打开pika-sensor 上的传感器（相机）</font>**<font style="color:#333333;">：</font>

| <font style="color:#333333;">1个sensor</font> | <font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_single_sensor.bash</font> |
| :--- | :--- |
| <font style="color:#333333;">1个gripper</font> | <font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_single_gripper.bash</font> |
| <font style="color:#333333;">2个sensor</font> | <font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_multi_sensor.bash</font> |
| <font style="color:#333333;">2个gripper</font> | <font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_multi_gripper.bash</font> |
| <font style="color:#333333;">1个sensor</font><br/><font style="color:#333333;">1个gripper</font> | <font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_sensor_gripper.bash</font> |
| <font style="color:#333333;">2个sensor</font><br/><font style="color:#333333;">2个gripper</font> | <font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_multi_sensor.bash sensor</font><br/><font style="color:#262626;">cd ~/pika_ros/scripts/ && bash start_multi_gripper.bash gripper sensor </font> |


## **<font style="color:#1a1a1a;">2.</font>****<font style="color:#1a1a1a;">9</font>****<font style="color:#1a1a1a;"> 摄像头参数配置（可选）</font>**
<font style="color:#333333;">我们默认给定的的摄像头分辨率为 640x480，帧率为 30 FPS</font><font style="color:#333333;">。</font>

<font style="color:#333333;">如果这不满足您的需求，可按照下面步骤修改摄像头配置参数。</font>

<font style="color:#333333;">我们提供了两种分辨率供选择：</font>

| <font style="color:#333333;">分辨率</font> | <font style="color:#333333;">帧率</font> |
| :---: | :---: |
| <font style="color:#333333;">640x480</font> | <font style="color:#333333;">30/60/90</font> |
| <font style="color:#333333;">1280x720</font> | <font style="color:#333333;">30</font> |


<font style="color:#333333;">运行：</font>

```plain
gedit ~/pika_ros/scripts/start_multi_sensor.bash
```

<font style="color:#333333;">结果如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442582124-d0bb5b3d-fe2f-436d-b031-c11104786af9.png" width="604" title="" crop="0,0,1,1" id="ua4300563" class="ne-image">

<font style="color:#333333;">在红框的参数中选择适合您的参数填入即可，camera_fps 为相机帧率，camera_width 为图像宽度，camera_height 为图像高度。</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

**<font style="color:#000000;">Pika Sense 以及Pika Gripper的参数配置一致。参考上述说明即可。</font>**

:::

# **<font style="color:#1a1a1a;">三、 Pika sense 使用说明</font>**
## **<font style="color:#1a1a1a;">3.1 设备连接</font>**
<font style="color:#333333;">Pika sense需要搭配基站使用，可以单独使用pika sense进行数据采集，也可以使用pika sense遥操作机械臂进行数据采集。</font><font style="color:#ff0000;">遥操作请参考【五、Pika遥操作机械臂】。</font><font style="color:#333333;">单独使用pika sense进行数据采集的连接方式如下图所示：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442582627-db07ed93-1a2e-4521-830a-e95ef5bed02b.png" width="604" title="" crop="0,0,1,1" id="u34414632" class="ne-image">

## **<font style="color:#1a1a1a;">3.2 开启设备</font>**
<font style="color:#333333;">可以使用一个sense进行数据采集，也可以使用两个sense进行数据采集，使用之前，请确保执行器电源已经上电。若使用左右双sense，</font><font style="color:#ff0000;">请参照2.6进行左右senseUSB设置</font>**<font style="color:#333333;">。</font>**<font style="color:#333333;">之后，</font>

<font style="color:#333333;">sense的打开方式如下：</font>

```plain
cd ~/pika_ros/scripts/
bash start_single_sensor.bash  # single sensor
bash start_multi_sensor.bash  # double sensor
```

<font style="color:#333333;">开启设备后，跳转至【六、数据采集】。</font>

## **<font style="color:#1a1a1a;">3.3 坐标说明</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442582773-f53c4bc8-9ab1-4cc0-a894-ee9e45709080.png" width="293" title="" crop="0,0,1,1" id="u8c29b7ae" class="ne-image">

<font style="color:#333333;">pika的坐标系是在夹爪中心上，通过 pika_pose 话题发布，话题类型为 geometry_msgs::PoseStamped</font>

<font style="color:#333333;">pika_pose 话题的坐标系如上图所示：x轴朝前、y轴朝左、z轴朝右。</font>

## **<font style="color:#1a1a1a;">3.4 话题说明</font>**
<font style="color:#333333;">单sense使用情况下，sense夹爪话题名为：/gripper_l/data，位姿话题名为：/pika_pose。</font>

<font style="color:#333333;">双sense使用情况下，左sense夹爪话题名为：/gripper_l/data，右sense夹爪话题名为：/gripper_r/data，左sense位姿话题名为：/pika_pose_l，右sense位姿话题名为：/pika_pose_r。</font>

<font style="color:#333333;">订阅夹爪信息：</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
ros2 topic echo /gripper/data  # single sensor
ros2 topic echo /gripper_l/data  # double sensor, left
ros2 topic echo /gripper_r/data  # double sensor, right
```

<font style="color:#333333;">输出数据如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442583104-8affc1fc-874c-49ea-9e49-9ae6e25f4c3d.png" width="590" title="" crop="0,0,1,1" id="uf379f48e" class="ne-image">

<font style="color:#333333;">或者：</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
ros2 topic echo /gripper/joint_states  # single sensor
ros2 topic echo /gripper_l/joint_states  # double sensor, left
ros2 topic echo /gripper_r/joint_states  # double sensor, right
```

<font style="color:#333333;">输出数据如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442583311-17c04bed-0a58-4a82-8436-8618a7ac594d.png" width="604" title="" crop="0,0,1,1" id="u593b16f8" class="ne-image">

# <font style="color:rgb(26, 26, 26);">新增、 Pika Helmet 使用说明</font>
## <font style="color:rgb(26, 26, 26);">开启设备</font>
<font style="color:rgb(38, 38, 38);">Helmet 有带定位器和不带定位器两种使用方式，在~/pika_ros/scripts/setup_device.py 中对 helmet 进行绑定时会提供这两种方式的绑定，请根据情况选择。</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/12455065/1779345896144-af5b735a-a496-4f4c-b4bb-a66e65112abe.png" width="367.27271931230547" title="" crop="0,0,1,1" id="u6c59a99c" class="ne-image"><font style="color:rgb(38, 38, 38);">  
</font>请参照2.6 对 helmet 进行绑定设置之后，使用下面的指令来开启设备：

```bash
cd ~/pika_ros/scripts/
bash start_helmet.bash 
```

<font style="color:rgb(38, 38, 38);">开启设备后，跳转至【六、数据采集】。</font>

# **<font style="color:#1a1a1a;">四、 Pika Gripper 使用说明</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442583602-237bf3ad-2796-4085-bf65-56547e1b8f97.jpeg" width="586" title="" crop="0,0,1,1" id="ub721811d" class="ne-image">

<font style="color:#333333;">如上图所示，为Pika Gripper单独使用流程。</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">使用之前说明：</font>**<font style="color:#333333;"></font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">Gripper可支持单独作为夹爪使用，非必须搭配Station与Sense使用。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">Gripper可支持搭配任意机械臂使用，非必须搭配Piper。</font>

<font style="color:#333333;">● Gripper可用于sense采集数据的推理。</font>

<font style="color:#333333;">● Gripper可用于sense遥操作机械臂。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#ff0000;">复用的通讯口（CAN口）未使用，通讯和控制接口统一使用Type-c接口进行通讯。</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#ff0000;">通信接口必须需使用USB3.0的接口。</font>**

:::

## **<font style="color:#1a1a1a;">4.1 结构组装</font>**
<font style="color:#333333;">	Pika Gripper适合多种操作器末端安装使用，这里以松灵机器人Piper机械臂举例说明，如下图所示，Gripper末端是预留了安装孔位，侧边预留4个M3螺纹通孔，需要借助法兰件进行拼接组装，法兰结构件需要根据机械臂或其他操作器末端安装孔位进行设计。（具体尺寸参见三维模型）</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442583829-8e6e8c7d-a739-415c-9354-0947b6f5045b.png" width="414" title="" crop="0,0,1,1" id="u1ad4dc1c" class="ne-image">

**<font style="color:#333333;">Pika Gripper 与第三方机械臂安装说明</font>****<font style="color:#333333;">：</font>**

<font style="color:#333333;">Gipper与其他机械臂安装时只需安装一个转接法兰，目前所有法兰能通用大部分工业级机械臂，特殊的机械臂也可以特别定制法兰。</font>

<font style="color:#333333;">安装步骤：</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">先将法兰安装到机械臂的末端</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">再将Pika Gripper与法兰安装</font>

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442584012-b3b27796-03d2-4ee4-bacc-d44e999ab922.jpeg" width="577" title="" crop="0,0,1,1" id="ufdaa3789" class="ne-image">

## **<font style="color:#1a1a1a;">4.2 电气连接</font>**
<font style="color:#000000;">电气连接：使用XT30系列母头插入Pika Gripper的XT30 2+2接口并通24V电源（线序参考下图）。供电接口类型为XT30(PB)，</font>**<font style="color:#ff0000;">其中复用的通讯口（CAN口）未使用，通讯和控制接口统一使用Type-c接口进行通讯</font>**<font style="color:#000000;">，使用时，使用一个</font>**<font style="color:#ff0000;">USB3.0</font>**<font style="color:#000000;">含以上的线束与夹爪相连接即可。电源接口以及接口定义如下表:</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442584822-a3fbe4a2-a2c7-42a7-9595-9766ef985c3a.png" width="250" title="" crop="0,0,1,1" id="u51e73f75" class="ne-image">

| <font style="color:#333333;">1</font> | <font style="color:#333333;">24V供电 -</font> | <font style="color:#333333;">4</font> | <font style="color:#333333;">CAN-H（预留）</font> |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">2</font> | <font style="color:#333333;">24V供电 +</font> | <font style="color:#333333;">5</font> | <font style="color:#333333;">TPYE-C</font> |
| <font style="color:#333333;">3</font> | <font style="color:#333333;">CAN-L（预留）</font> | <font style="color:#333333;">---</font> | <font style="color:#333333;">---</font> |


## **<font style="color:#1a1a1a;">4.3 通讯连接</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442585241-cf4b575c-f934-4d5a-93d5-b6ada828b6bb.png" width="250" title="" crop="0,0,1,1" id="uaf209956" class="ne-image">

<font style="color:#000000;">通讯连接：如上图5位置Type-C线束连接至PC。</font>

<font style="color:#333333;">若自行准备电脑与采集器（Pika Sense）相连接，其电脑软/硬件需求如下：</font>

| <font style="color:#333333;">软/硬件要求</font> | <font style="color:#333333;">参考参数</font> |
| :---: | :---: |
| <font style="color:#333333;">PC 芯片架构</font> | <font style="color:#333333;">X86</font> |
| <font style="color:#333333;">PC 存储空间</font> | <font style="color:#333333;">建议1TB以上</font> |
| <font style="color:#333333;">PC 接口</font> | <font style="color:#333333;">USB3.1 x 3</font> |
| <font style="color:#333333;">操作系统</font> | <font style="color:#333333;">Ubuntu20.04</font> |
| <font style="color:#333333;">ROS 版本</font> | <font style="color:#333333;">ROS2-humble</font> |


## **<font style="color:#1a1a1a;">4.4 执行器的使用ROS包</font>**
:::warning
<font style="color:#333333;">此处主要说明模型推理时如何获取夹爪数据以及控制夹爪，</font><font style="color:#ff0000;">若要使用遥操作，请跳转【五、Pika遥操作机械臂】</font><font style="color:#333333;">。</font>

<font style="color:#333333;">使用执行器之前，请确保执行器电源已经上电。</font><font style="color:#ff0000;">若使用左右双执行器，请参照2.6进行左右</font><font style="color:#ff0000;">执行器USB设置</font><font style="color:#333333;">。</font>

:::

<font style="color:#333333;">之后，开启鱼眼摄像头、pikaDepthCamera和电机控制串口：</font>

```plain
cd ~/pika_ros/scripts/
bash start_single_gripper.bash  # single gripper
bash start_multi_gripper.bash  # double gripper
```

<font style="color:#333333;">控制电机：</font>

<font style="color:#333333;">1.</font><font style="color:#333333;"> </font><font style="color:#333333;">失能：发布话题/gripper/ctrl消息如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442586157-bb66c200-7304-4202-b46e-ae620c18b994.png" width="604" title="" crop="0,0,1,1" id="u0ad8c2bb" class="ne-image">

<font style="color:#333333;">双执行器情况下，左执行器话题为/gripper_l/ctrl，右执行器话题为/gripper_r/ctrl。</font>

<font style="color:#333333;">2.</font><font style="color:#333333;"> </font><font style="color:#333333;">使能：发布话题/gripper/ctrl如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442586562-1da14f82-db03-4767-8e8b-dda640bc5f55.png" width="604" title="" crop="0,0,1,1" id="ufb34d9d0" class="ne-image">

<font style="color:#333333;">双执行器情况下，左执行器话题为/gripper_l/ctrl，右执行器话题为/gripper_r/ctrl。</font>

<font style="color:#333333;">3.</font><font style="color:#333333;"> </font><font style="color:#333333;">控制电机角度：发布话题/gripper/ctrl消息如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442587056-87f58d0e-cd8c-4716-9acc-427203fc86c9.png" width="608" title="" crop="0,0,1,1" id="uf24f541f" class="ne-image">

<font style="color:#333333;">双执行器情况下，左执行器话题为/gripper_l/ctrl，右执行器话题为/gripper_r/ctrl。</font>

<font style="color:#333333;">或者发布话题/joint_states消息如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442587408-4abf6665-3853-4a32-8782-330d886f0a92.png" width="604" title="" crop="0,0,1,1" id="ub3bd0101" class="ne-image">

<font style="color:#333333;">双执行器情况下，左执行器话题为/joint_states_l，右执行器话题为/joint_states_r。</font>

<font style="color:#333333;">4.</font><font style="color:#333333;"> </font><font style="color:#333333;">设置零点：请先使能之后，将夹爪闭合，再设置零点。发布话题/gripper/ctrl消息如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442587502-d2cc700a-015b-437d-9d8c-23d3f5f4cc1d.png" width="604" title="" crop="0,0,1,1" id="u061e7853" class="ne-image">

<font style="color:#333333;">双执行器情况下，左执行器话题为/gripper_l/ctrl，右执行器话题为/gripper_r/ctrl。</font>

<font style="color:#333333;">订阅电机信息：</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
ros2 topic echo /gripper/data  # single gripper
ros2 topic echo /gripper_l/data  # double gripper, left
ros2 topic echo /gripper_r/data  # double gripper, right
```

<font style="color:#333333;">输出数据如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442587395-4b888e98-d407-4570-ac64-7cca875b9b02.png" width="593" title="" crop="0,0,1,1" id="ue8ce265d" class="ne-image">

<font style="color:#333333;">或者：</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
ros2 topic echo /gripper/joint_states  # single gripper
ros2 topic echo /gripper_l/joint_states  # double gripper, left
ros2 topic echo /gripper_r/joint_states  # double gripper, right
```

<font style="color:#333333;">输出数据如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442587638-ef38af74-c06e-414a-9dbb-2e358d8e90f6.png" width="604" title="" crop="0,0,1,1" id="u7cee3aad" class="ne-image">

## **<font style="color:#1a1a1a;">4.5 执行器的参数说明</font>**
<font style="color:#333333;">相机到夹爪中心的距离（单位：mm），无任何偏转，如下图所示：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1752219313121-2705554b-0fcb-458d-86cf-2b92943cbb2f.png" width="1348.6666666666667" title="" crop="0,0,1,1" id="u4263cff2" class="ne-image">

<font style="color:#333333;">可由此得到各相机到夹爪中心的变换矩阵。</font>

# **<font style="color:#1a1a1a;">五、</font>****<font style="color:#1a1a1a;"> </font>****<font style="color:#1a1a1a;">Pika 遥操作机械臂</font>**
**<font style="color:#333333;">如下图所示为Pika Sense、Pika Station、Piper 两指夹爪结合进行遥操采集（Pika Gripper适配中，参考如上示例可实现Pika Sense、Pika Station搭配其他任意臂进行遥操作。</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442588268-ea9c1994-db46-472e-8476-7c59aef283cb.jpeg" width="746" title="" crop="0,0,1,1" id="u8f44ff9e" class="ne-image">

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#ff0000;">目前Pika sense的遥操作只适配了AgileX Piper、 Xarm Lite 6机械臂，其他的第三方机械臂需要开发者和用户自行适配。 也欢迎开发者和用户进行适配，适配完成以后欢迎在我们的Github 提交Pr，审核通过以后，我们会合并代码，与大家共建Pika产品生态。</font>

:::

## **<font style="color:#1a1a1a;">5.1 硬件准备</font>**
**<font style="color:#333333;">遥操作单个Piper + Piper 默认配置夹爪 </font>**

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">机械臂组装时红点朝向与下面线缆红点对应，航插带纹路部位为受力向后可收缩区域，在安装时红点向下对准凸点直接插入即可，拔出时在纹路部分按下后拔出即可。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">遥操作单个Piper + Pika Gripper 尚在更新中</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">遥操作第三方机械臂准备（参照PIPER步骤执行即可）</font>

:::

**<font style="color:#333333;">第一步：完成Piper连接 </font>**<font style="color:#333333;">Piper的的连接说明与示意图如下，更详细接线参照PIPER使用手册。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442588092-9a51d64e-33dd-4317-9404-2c180eb37ac6.png" width="604" title="" crop="0,0,1,1" id="u61db978a" class="ne-image">

<font style="color:#000000;">机械臂第一次上电需要按照以下A-G顺序进行操作：</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">1、先把A的J2连接口插上；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">2、把航空插头B的CAN线接好；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">3、把C的XT30接头对插好；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">4、把D航空插头红点向下对插好；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">5、把适配器E的插头插好；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">6、检查确认适配器E的AC头插好上电，待电器面板指示灯闪烁绿色后；</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#000000;">7、把USB线插进电脑进行使用。</font>

**<font style="color:#333333;">第二步：完成Pika Sense的连接</font>**

<font style="color:#333333;">Pika Sense接口说明与连接示意图，参见本文档2.1/2.2/2.3。</font>

## **<font style="color:#1a1a1a;">5.2 软件准备</font>**
<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

<font style="color:#333333;">1、安装环境依赖</font>

```plain
sudo apt update && sudo apt install ethtool
sudo apt update && sudo apt install can-utils
```

<font style="color:#333333;">2、自行安装 miniconda 或 Anaconda</font>

<font style="color:#333333;">3、安装环境依赖</font>

```plain
conda create -n pika python=3.10
conda activate pika
conda install pinocchio==3.2.0 casadi==3.6.7 -c conda-forge
pip install lark numpy==2.0.2 empy==3.3.4 meshcat pyyaml pyagxarm opencv-python netifaces catkin_pkg
```

## **<font style="color:#1a1a1a;">5.3 开始摇操</font>**
### **<font style="color:#1a1a1a;">5.3.1 单臂遥操</font>**
<font style="color:#333333;">1、机械臂使能</font>

<font style="color:#333333;">将机械臂的can线接入电脑</font>

<font style="color:#333333;">然后执行：</font>

```plain
cd ~/pika_ros/src/PikaAnyArm/agx_arm/agx_arm_ros/scripts

bash can_activate.sh 
```

<font style="color:#333333;">2、对pika进行校准，详细步骤可参考 Pika 产品用户手册的 【2.1 基站部署】和【2.5 定位基站校准】</font>

<font style="color:#333333;">3、开启遥操单Piper程序</font>

<font style="color:#333333;">3-1、若只使用pika sense，不使用pika gripper或使用piper原装夹爪。则</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

<font style="color:#333333;">终端1：</font>

```plain
conda deactivate
source ~/pika_ros/install/setup.bash
cd ~/pika_ros/scripts && bash start_single_sensor_whit_teleop.bash
```

<font style="color:#333333;">终端 2：</font>

```plain
source ~/pika_ros/install/setup.bash
conda activate pika
# piper
ros2 launch pika_remote_agx_arm teleop_single_piper.launch.py
# piper_x
ros2 launch pika_remote_agx_arm teleop_single_piper_x.launch.py
# nero
ros2 launch pika_remote_agx_arm teleop_single_nero.launch.py
```

<font style="color:#333333;">最后，双击右手 sense 夹爪以开启遥操作。</font>

:::warning
<font style="color:#ff0000;">注意：双击时请保持sense的姿态与机械臂末端一致！</font>

:::

<font style="color:#333333;">3-2、若将pika gripper安装于机械臂上，使用sense控制gripper，请参照【2.6 设备绑定】绑定1个sense和1个gripper。之后，</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

<font style="color:#333333;">终端1：</font>

```plain
conda deactivate
source ~/pika_ros/install/setup.bash
cd ~/pika_ros/scripts && bash start_sensor_gripper.bash
```

<font style="color:#333333;">终端 2：</font>

```plain
source ~/pika_ros/install/setup.bash
conda activate pika
ros2 launch pika_remote_agx_arm teleop_rand_single_piper.launch.py
# piper
ros2 launch pika_remote_agx_arm teleop_single_piper.launch.py
# piper_x
ros2 launch pika_remote_agx_arm teleop_single_piper_x.launch.py
# nero
ros2 launch pika_remote_agx_arm teleop_single_nero.launch.py
```

<font style="color:rgb(51, 51, 51);">最后，双击右手 sense 夹爪以开启遥操作。</font>

:::warning
<font style="color:#ff0000;">注意：双击时请保持sense的姿态与机械臂末端一致！</font>

:::

### **<font style="color:#1a1a1a;">5.3.2 双臂遥操</font>**
<font style="color:#333333;">1、机械臂使能</font>

<font style="color:#333333;">先将左机械臂的can线接入电脑</font>

<font style="color:#333333;">然后执行：</font>

```plain
cd ~/pika_ros/src/PikaAnyArm/agx_arm/agx_arm_ros/scripts

bash find_all_can_port.sh
```

<font style="color:#333333;">终端会出现左机械臂的端口号，接着将右机械臂的can线接入电脑</font>

<font style="color:#333333;">再次执行：</font>

```plain
bash find_all_can_port.sh
```

<font style="color:#333333;">终端会出现右机械臂的端口号。</font>

<font style="color:#333333;">将这左右两个端口号复制到 can_config.sh 文件的 111 和 112 行，如下所示：</font>

```plain
if [ "$EXPECTED_CAN_COUNT" -ne 1 ]; then
    declare -A USB_PORTS 
    USB_PORTS["1-8.1:1.0"]="left_piper:1000000"  #左机械臂
    USB_PORTS["1-8.2:1.0"]="right_piper:1000000" #右机械臂
fi
```

<font style="color:#333333;">保存完毕后，激活左右机械臂使能脚本：</font>

```plain
cd ~/pika_ros/src/PikaAnyArm/agx_arm/agx_arm_ros/scripts

bash can_config.sh
```

<font style="color:#333333;">2、对pika进行校准，详细步骤可参考 Pika 产品用户手册 的 【2.1 基站部署】和【2.5 定位基站校准】，最后是 【2.7 设置左右手定位器】对左右定位器进行绑定。</font>

<font style="color:#333333;">3、开启遥操程序</font>

<font style="color:#333333;">3-1、若只使用pika sense，不使用pika gripper或使用piper原装夹爪。请参照【2.6 设备绑定】绑定左右2个sense。之后，</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

<font style="color:#333333;">终端1：</font>

```plain
conda deactivate
source ~/pika_ros/install/setup.bash
cd ~/pika_ros/scripts && bash start_multi_sensor_whit_teleop.bash sensor
```

<font style="color:#333333;">终端2：</font>

```plain
source ~/pika_ros/install/setup.bash
conda activate pika
# piper
ros2 launch pika_remote_agx_arm teleop_double_piper.launch.py
# piper_x
ros2 launch pika_remote_agx_arm teleop_double_piper_x.launch.py
# nero
ros2 launch pika_remote_agx_arm teleop_double_nero.launch.py
```

<font style="color:rgb(51, 51, 51);">最后，双击右手 sense 夹爪以开启遥操作。</font>

:::warning
<font style="color:#ff0000;">注意：双击时请保持sense的姿态与机械臂末端一致！</font>

:::

<font style="color:#333333;">3-2、若将pika gripper安装于机械臂上，使用sense控制gripper。请参照【2.6 设备绑定】绑定左右2个sense和左右2个gripper。之后，</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

<font style="color:#333333;">终端1：</font>

```plain
conda deactivate
source ~/pika_ros/install/setup.bash
cd ~/pika_ros/scripts && bash start_multi_sensor_whit_teleop.bash sensor
```

<font style="color:#333333;">终端2：</font>

```plain
conda deactivate
source ~/pika_ros/install/setup.bash
cd ~/pika_ros/scripts && bash start_multi_gripper.bash gripper sensor
```

<font style="color:#333333;">终端3：</font>

```plain
source ~/pika_ros/install/setup.bash
conda activate pika
# piper
ros2 launch pika_remote_agx_arm teleop_double_piper.launch.py
# piper_x
ros2 launch pika_remote_agx_arm teleop_double_piper_x.launch.py
# nero
ros2 launch pika_remote_agx_arm teleop_double_nero.launch.py
```

<font style="color:rgb(51, 51, 51);">最后，双击右手 sense 夹爪以开启遥操作。</font>

:::warning
<font style="color:#ff0000;">注意：双击时请保持sense的姿态与机械臂末端一致！</font>

:::



## **<font style="color:#1a1a1a;">5.3 配置文件说明</font>**
<font style="color:#333333;">在 config 文件夹中：</font>

<font style="color:#333333;">1、piper_params.yaml 中的：</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;"> gripper_xyzrpy 指的是夹爪相对于机器人joint6的偏移量，单位是米和弧度。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;"> target_joint_state 指的是机械臂初始位姿的6个关节角度，单位为弧度。</font>

<font style="color:#333333;">2、xarm_params.yaml 中的：</font>

<font style="color:#333333;">● eff_position 指的是机械臂的执行器初始位置和方向，单位是毫米和弧度。</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">pika_to_arm 指的是从pika夹爪中心坐标系到机械臂末端执行器坐标系的转换，单位是米和弧度。</font>

## **<font style="color:#1a1a1a;">5.4 坐标说明</font>**
<font style="color:#333333;">为了方便使用 pika sense 遥操自己的机械臂，我们在此说明：</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">pika 夹爪末端坐标系</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font><font style="color:#333333;">pika_pose 话题信息</font>

### **<font style="color:#1a1a1a;">5.4.1 pika坐标系图</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442588789-0fef5bd1-2df0-4e29-a3dc-10c84fcabf7e.png" width="293" title="" crop="0,0,1,1" id="u53bec4dc" class="ne-image">

<font style="color:#333333;">pika的坐标系是在夹爪中心上，通过 pika_pose 话题发布。</font>

<font style="color:#333333;">在通过双击操作后，会将双击时  pika sense 的坐标设置为零点，往后的移动的量都是相对该零点，</font>

<font style="color:#333333;">此时：pika_pose 话题的坐标系如上图所示：x轴朝前、y轴朝左、z轴朝上。</font>

### **<font style="color:#1a1a1a;">5.4.2 话题信息</font>**
<font style="color:#333333;">单个 pika sense 遥操下发控制机械臂的话题名为：/pika_pose，左右手 pika sense遥操下发话题分别对应：/pika_pose_l、/pika_pose_r。</font>

<font style="color:#333333;">/pika_pose 话题的数据类型为 geometry_msgs::PoseStamped，市场主流机械臂一般都会开放机械臂末端控制接口，其消息类型也是 geometry_msgs::PoseStamped</font>

<font style="color:#333333;">代码可以参考：teleop_xarm.py</font>[PikaAnyArm/pika_remote_piper/scripts/teleop_xarm.py at master · agilexrobotics/PikaAnyArm · GitHub](https://github.com/agilexrobotics/PikaAnyArm/blob/master/remote_operation/scripts/teleop_xarm.py)

# **<font style="color:#1a1a1a;">六、</font>****<font style="color:#1a1a1a;"> </font>****<font style="color:#1a1a1a;">数据采集</font>**
:::warning
**<font style="color:#c00000;">注意：以下涉及到遥操作的数据采集代码都为两个pika sense以及两个pika gripper的情况。若有其它情况，需至~/pika_ros/install/share/data_tools/config中添加相应的需要采集的话题yaml文件，并在数据采集的时候使用type:=yaml前缀进行配置。如何修改请参考github仓库，数据采集相关代码更新于</font>**[GitHub - agilexrobotics/data_tools](https://github.com/agilexrobotics/data_tools.git)**<font style="color:#c00000;">，相关问题可以提交issue。</font>**

**<font style="color:#DF2A3F;">不能把不同的数据放在同一个目录下，不然无法完成数据同步和转化。</font>**

**<font style="color:#c00000;">注意：若采集数据的程序开启后自动关闭，请按照提示，使用rostopic hz {话题名称}检查设备帧率，确保设备正常运行。</font>**

:::

## **<font style="color:#1a1a1a;">6</font>****<font style="color:#1a1a1a;">.1 启动软件</font>**
<font style="color:#333333;">请按照需要打开软件，遥操作参考【五、pika遥操作机械臂】，pika数据采集请参考【三、pika sense 使用说明】。</font>

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：此处出现如下</font>****<font style="color:#333333;">报错，按照下列方法解决</font>**<font style="color:#ff0000;">/home/name/pika_ros/install/lib/librealsense2_camera.so: undefined symbol: _ZN20ddynamic_reconfigure19DDynamicReconfigureC1ERKN3ros10NodeHandleE</font>

**<font style="color:#333333;">A: </font>**<font style="color:#333333;">这个问题产生的原因是</font><font style="color:#333333;">ros-noetic-ddynamic-reconfigure该模块默认安装的是最新版本，由于版本更新，导致不可用。可用版本已放到pika_ros/source/下。名称为：ros-noetic-ddynamic-reconfigure_0.3.2-1focal.20240913.193805_amd64.deb，使用dpkg 安装即可：</font><font style="color:#333333;">sudo dpkg -i ros-noetic-ddynamic-reconfigure_0.3.2-1focal.20240913.193805_amd64.deb </font>

:::

<font style="color:#333333;">启动代码后，rviz界面中显示 pika 的tf坐标:</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442588866-333bbecb-d1b0-406f-ae2d-f8bf08869359.png" width="604" title="" crop="0,0,1,1" id="u284e18c9" class="ne-image">

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">注意：</font>**

**<font style="color:#000000;">在rviz中确保pika的tf变换不抖动不异常。</font>**

**<font style="color:#000000;">如在无遮挡的情况下仍然出现明显的抖动，则需要再次进行定位校准。</font>**

:::

## **<font style="color:#1a1a1a;">6</font>****<font style="color:#1a1a1a;">.2 数据采集</font>**
<font style="color:#333333;">软件启动完成后，</font><font style="color:#333333;">运行以下命令进行数据采集。其中</font><font style="color:#333333;">datasetDir</font><font style="color:#333333;">参数为数据目录；</font>

<font style="color:#333333;">episodeIndex参数为数据组别，通常采用每组数据递增方式，设置为0即为第0组。</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
source ~/pika_ros/install/setup.sh 
ros2 launch data_tools run_data_capture.launch.py type:=single_pika datasetDir:=$HOME/agilex/data episodeIndex:=0  # 单夹持器
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py type:=multi_pika datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器
ros2 launch data_tools run_data_capture.launch.py type:=single_helmet datasetDir:=$HOME/agilex/data episodeIndex:=0  # 头盔（不带定位器）
ros2 launch data_tools run_data_capture.launch.py type:=single_helmet_whit_tracker datasetDir:=$HOME/agilex/data episodeIndex:=0  # 头盔（带定位器）
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py type:=multi_pika_helmet datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器+头盔(不带定位器）
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py type:=multi_pika_helmet_with_tracker datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器+头盔(带定位器）
ros2 launch data_tools run_data_capture.launch.py type:=single_pika_teleop datasetDir:=$HOME/agilex/data episodeIndex:=0  # 单夹持器遥操作
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py type:=multi_pika_teleop datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器遥操作
```

<font style="color:#333333;">若想使用双击开启数据采集的情况，请在</font><font style="color:#000000;">ros2 launch data_tools run_data_capture.launch 后添加参数 useService:=true，如：</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
source ~/pika_ros/install/setup.sh 
ros2 launch data_tools run_data_capture.launch.py useService:=true type:=single_pika datasetDir:=$HOME/agilex/data episodeIndex:=0  # 单夹持器
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py useService:=true type:=multi_pika datasetDir:=$HOME/agilex/data episodelndex:=0 #双夹持器
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py useService:=true type:=multi_pika_helmet datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器+头盔(不带定位器）
ros2 launch data_tools run_data_capture_whit_double_pika_teleop.launch.py useService:=true type:=multi_pika_helmet_with_tracker datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器+头盔(带定位器）
ros2 launch data_tools run_data_capture.launch.py useService:=true type:=single_pika_teleop datasetDir:=$HOME/agilex/data episodeIndex:=0  # 单夹持器遥操作
ros2 launch data_tools run_data_capture_whit_double_pika.launch.py useService:=true type:=multi_pika_teleop datasetDir:=$HOME/agilex/data episodeIndex:=0  # 双夹持器遥操作
```

<font style="color:#333333;">注：只有带有 pika sense 的情况才能使用双击开启采集，只有 helmet 的情况无法用该方法开启采集。</font>

<font style="color:#333333;">若采集程序成功开启，终端显示如下：</font>

<font style="color:#000000;background-color:#fafafa;">path: /home/agilex/data/episode0</font>

<font style="color:#000000;background-color:#fafafa;">total time: 7.0014 </font>

<font style="color:#000000;background-color:#fafafa;">topic: frame in 1 second / total frame </font>

<font style="color:#000000;background-color:#fafafa;">/camera/color/image_raw: 0 / 165 </font>

<font style="color:#000000;background-color:#fafafa;">/camera_fisheye/color/image_raw: 0 / 0 </font>

<font style="color:#000000;background-color:#fafafa;">/camera/depth/image_rect_raw: 0 / 165 </font>

<font style="color:#000000;background-color:#fafafa;">/</font><font style="color:#000000;background-color:#fafafa;">pika_pose</font><font style="color:#000000;background-color:#fafafa;">: 0 / 0 </font>

<font style="color:#000000;background-color:#fafafa;">/gripper/data: 0 / 367 </font>

<font style="color:#000000;background-color:#fafafa;">sum total frame: 1229 </font>

<font style="color:#333333;">请在采集过程中确保每个话题的“</font><font style="color:#333333;">frame in 1 second</font><font style="color:#333333;">”符合传感器数据频率。</font>

<font style="color:#333333;">按下Enter按钮结束采集，显示如下为采集结束</font>

<font style="color:#000000;background-color:#fafafa;">Done </font>

<font style="color:#000000;background-color:#fafafa;">[data_tools_dataCapture-1] process has finished cleanly </font>

<font style="color:#000000;background-color:#fafafa;">log file: /home/noetic/.ros/log/21114750-1995-11ef-b6f1-578b5ce9ba2e/data_tools_dataCapture-1*.log </font>

<font style="color:#000000;background-color:#fafafa;">all processes on machine have died, roslaunch will exit </font>

<font style="color:#000000;background-color:#fafafa;">shutting down processing monitor... </font>

<font style="color:#000000;background-color:#fafafa;">... shutting down processing monitor complete </font>

<font style="color:#000000;background-color:#fafafa;">done</font>

:::warning
<font style="color:#ff0000;">注意：以上为个例说明，不同的采集方式会出现不同的话题名称等！若出现程序中断无法运行的情况，请使用</font>

:::

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
ros2 topic hz {终端显示的需要检查的话题}
```

<font style="color:#ff0000;">检查话题帧率，拔插出现问题的设备重新开启设备。</font>

<font style="color:#333333;">数据示例：</font><font style="color:#ff0000;">（个例</font><font style="color:#ff0000;">说明）</font>

<font style="color:#333333;">保存数据目录：</font>

| **<font style="color:#333333;">地址</font>** | **<font style="color:#333333;">数据类型</font>** | **<font style="color:#333333;">说明</font>** |
| --- | :---: | :---: |
| <font style="color:#333333;">/home/agilex/data/episode0/camera/color/pikaDepthCamera</font> | <font style="color:#333333;">.png</font> | <font style="color:#333333;">pikaDepthCamera摄像头RGB数据路径</font> |
| <font style="color:#333333;">/home/agilex/data/episode0/camera/color/fisheye</font> | <font style="color:#333333;">.png</font> | <font style="color:#333333;">鱼眼摄像头RGB数据路径</font> |
| <font style="color:#333333;">/home/agilex/data/episode0/camera/depth/pikaDepthCamera</font> | <font style="color:#333333;">.png</font> | <font style="color:#333333;">pikaDepthCamera摄像头深度数据路径</font> |
| <font style="color:#333333;">/home/agilex/data/episode0/localization/pose/pikaLocator</font> | <font style="color:#333333;">.json</font> | <font style="color:#333333;">定位器定位数据</font><br/><font style="color:#333333;">（位姿x、y、z、roll、pitch、yaw）</font> |
| <font style="color:#333333;">/home/agilex/data/episode0/gripper/encoder/pika</font> | <font style="color:#333333;">.json</font> | <font style="color:#333333;">夹爪开合数据</font><br/><font style="color:#333333;">（电机角度angle、夹爪距离distance）</font> |


<font style="color:#333333;">以pikaDepthCamera的RGB数据为例子，以时间戳作为文件名称，其结构如下：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442589267-15da966d-1c1a-46e2-b2c7-607ee399fbcd.png" width="798" title="" crop="0,0,1,1" id="u55e84e9b" class="ne-image">

:::warning
**<font style="color:#000000;">⚠</font>****<font style="color:#000000;">数据采集过程中常见异常处理</font>**

<font style="color:#000000;">●</font><font style="color:#000000;"> </font><font style="color:#000000;">Q：采集的数据帧率异常？</font>

<font style="color:#000000;">A : 请优先检查线束连接稳定性，重新线束插拔后检查数据帧率。</font>

:::

# **<font style="color:#1a1a1a;">七</font>****<font style="color:#1a1a1a;">、数据处理</font>**
## **<font style="color:#1a1a1a;">7</font>****<font style="color:#1a1a1a;">.1 数据同步</font>**
<font style="color:#333333;">运行以下命令进行数据同步。其中datasetDir参数为数据目录；episodeIndex参数为需要同步数据的组别，若为-1则同步datasetDir目录下的所有数据组。</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
source ~/pika_ros/install/setup.sh 
ros2 launch data_tools run_data_sync.launch.py type:=single_pika datasetDir:=$HOME/agilex/data/ episodeIndex:=-1  # 单夹持器
ros2 launch data_tools run_data_sync.launch.py type:=multi_pika datasetDir:=$HOME/agilex/data/ episodeIndex:=-1  # 双夹持器
ros2 launch data_tools run_data_sync.launch.py type:=single_pika_teleop datasetDir:=$HOME/agilex/data/ episodeIndex:=-1  # 单夹持器遥操作
ros2 launch data_tools run_data_sync.launch.py type:=multi_pika_teleop datasetDir:=$HOME/agilex/data/ episodeIndex:=-1  # 双夹持器遥操作
```

<font style="color:#DF2A3F;">(不使用 ROS 环境)</font>

```plain
python3 data_sync.py --type single_pika --datasetDir $HOME/agilex/data/  # 单夹持器
python3 data_sync.py --type multi_pika --datasetDir $HOME/agilex/data/  # 双夹持器
python3 data_sync.py --type single_pika_teleop --datasetDir $HOME/agilex/data/  # 单夹持器遥操作
python3 data_sync.py --type multi_pika_teleop --datasetDir $HOME/agilex/data/  # 双夹持器遥操作
```

<font style="color:#333333;">同步完成之后，将在每个特定数据路径中生成一个sync.txt文件。例如，图像数据同步索引文件路径：/home/agilex/data/episode0/camera/color/pikaDepthCamera/sync.txt。</font>

<font style="color:#333333;">sync.txt文件说明：</font>

<font style="color:#333333;">以pikaDepthCamera的RGB数据为例子，其sync.txt文件如下所示。其中包含了文件名，各个传感器同步后的sync.txt行数一致，为同步后的结果。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442590382-9e8eef25-7689-4e05-a659-0eb92b1c686e.png" width="914" title="" crop="0,0,1,1" id="udc03018b" class="ne-image">

## **<font style="color:#1a1a1a;">7</font>****<font style="color:#1a1a1a;">.2 数据转换</font>**
<font style="color:#333333;">7</font><font style="color:#333333;">.2.1 数据转换HDF5</font>

<font style="color:#333333;">运行以下命令在每个episode路径下生成data.hdf5文件。其中</font><font style="color:#333333;">datasetDir</font><font style="color:#333333;">参数为数据目录。</font>

<font style="color:#333333;">若使用点云，先进行点云转换：</font>

```plain
cd ~/pika_ros/scripts
python3 camera_point_cloud_filter.py --type single_pika --datasetDir $HOME/agilex/data/  # 单夹持器
python3 camera_point_cloud_filter.py --type multi_pika --datasetDir $HOME/agilex/data/  # 双夹持器
python3 camera_point_cloud_filter.py --type single_pika_teleop --datasetDir $HOME/agilex/data/  # 单夹持器遥操作
python3 camera_point_cloud_filter.py --type multi_pika_teleop --datasetDir $HOME/agilex/data/  # 双夹持器遥操作
```

<font style="color:#333333;">之后，转换HDF5：</font>

```plain
cd ~/pika_ros/scripts
python3 data_to_hdf5.py --type single_pika --datasetDir $HOME/agilex/data/  # 单夹持器
python3 data_to_hdf5.py --type multi_pika --datasetDir $HOME/agilex/data/  # 双夹持器
python3 data_to_hdf5.py --type single_pika_teleop --datasetDir $HOME/agilex/data/  # 单夹持器遥操作
python3 data_to_hdf5.py --type multi_pika_teleop --datasetDir $HOME/agilex/data/  # 双夹持器遥操作
```

<font style="color:#333333;">若不使用点云，直接转换HDF5：</font>

```plain
cd ~/pika_ros/scripts
python3 data_to_hdf5.py --type single_pika --datasetDir $HOME/agilex/data/ --useCameraPointCloud ""  # 单夹持器
python3 data_to_hdf5.py --type multi_pika --datasetDir $HOME/agilex/data/ --useCameraPointCloud ""  # 双夹持器
python3 data_to_hdf5.py --type single_pika_teleop --datasetDir $HOME/agilex/data/ --useCameraPointCloud ""  # 单夹持器遥操作
python3 data_to_hdf5.py --type multi_pika_teleop --datasetDir $HOME/agilex/data/ --useCameraPointCloud ""  # 双夹持器遥操作
```

<font style="color:#333333;">data.hdf5文件包含同步的图像路径索引、位姿数据等。</font>

<font style="color:#333333;">文件说明</font><font style="color:#333333;">（个例说明，此处无法列举所有情况，请自行读取文件查看数据内容）</font><font style="color:#333333;">：</font>

| **<font style="color:#333333;">字段</font>** | **<font style="color:#333333;">类型</font>** | **<font style="color:#333333;">维度</font>** | **<font style="color:#333333;">说明</font>** |
| :---: | :---: | :---: | :---: |
| <font style="color:#333333;">camera/color/</font><font style="color:#333333;">pikaDepthCamera</font> | <font style="color:#333333;">S</font><font style="color:#333333;">tring</font> | <font style="color:#333333;">(n,)</font> | <font style="color:#333333;">pikaDepthCamera摄像头RGB数据路径</font> |
| <font style="color:#333333;">camera/color/</font><font style="color:#333333;">fisheye</font> | <font style="color:#333333;">S</font><font style="color:#333333;">tring</font> | <font style="color:#333333;">(n,)</font> | <font style="color:#333333;">鱼眼摄像头RGB数据路径</font> |
| <font style="color:#333333;">camera/</font><font style="color:#333333;">depth</font><font style="color:#333333;">/</font><font style="color:#333333;">pikaDepthCamera</font> | <font style="color:#333333;">S</font><font style="color:#333333;">tring</font> | <font style="color:#333333;">(n,)</font> | <font style="color:#333333;">pikaDepthCamera摄像头深度数据路径</font> |
| <font style="color:#333333;">camera/</font><font style="color:#333333;">pointCloud</font><font style="color:#333333;">/</font><font style="color:#333333;">pikaDepthCamera</font> | <font style="color:#333333;">S</font><font style="color:#333333;">tring</font> | <font style="color:#333333;">(n,)</font> | <font style="color:#333333;">pikaDepthCamera摄像头点云数据路径</font> |
| <font style="color:#333333;">localization/pose/</font><font style="color:#333333;">pikaLocator</font> | <font style="color:#333333;">F</font><font style="color:#333333;">loat</font> | <font style="color:#333333;">(n,6)</font> | <font style="color:#333333;">定位器定位数据x\y\z\roll\pitch\yaw</font> |
| <font style="color:#333333;">gripper/encoderDistance/</font><font style="color:#333333;">pika</font> | <font style="color:#333333;">F</font><font style="color:#333333;">loat</font> | <font style="color:#333333;">(n,)</font> | <font style="color:#333333;">夹爪开合电机角度angle</font> |
| <font style="color:#333333;">size</font> | <font style="color:#333333;">I</font><font style="color:#333333;">nt</font> | <font style="color:#333333;">(n,)</font> | <font style="color:#333333;">数据的采集步长</font> |


<font style="color:#333333;">默认情况下，HDF5中的颜色、深度和点云使用文件索引，因此仍需要保留原始数据文件。如果不想使用索引，可以使用以下命令：</font>

```plain
cd ~/pika_ros/scripts
python3 data_to_hdf5.py --type single_pika --datasetDir {data_path} --useIndex "" --useCameraPointCloud "" --datasetTargetDir {hdf5_saving_path}    # 单夹持器
python3 data_to_hdf5.py --type multi_pika --datasetDir {data_path} --useIndex "" --useCameraPointCloud "" --datasetTargetDir {hdf5_saving_path}  # 双夹持器
python3 data_to_hdf5.py --type single_pika_teleop --datasetDir {data_path} --useIndex "" --useCameraPointCloud "" --datasetTargetDir {hdf5_saving_path}    # 单夹持器遥操作
python3 data_to_hdf5.py --type multi_pika_teleop --datasetDir {data_path} --useIndex "" --useCameraPointCloud "" --datasetTargetDir {hdf5_saving_path}  # 双夹持器遥操作
```

<font style="color:#333333;">{hdf5_saving_path}为要保存HDF5的路径。</font>

## **<font style="color:#1a1a1a;">7</font>****<font style="color:#1a1a1a;">.</font>****<font style="color:#1a1a1a;">3</font>****<font style="color:#1a1a1a;"> 数据重播</font>**
<font style="color:#333333;">请确保数据已经完成同步。</font>

<font style="color:#333333;">运行以下命令以读取sync.txt的方式进行数据重播。其中datasetDir参数为数据目录；episodeIndex参数为需要重播的数据组别。</font>

<font style="color:#DF2A3F;">(ubuntu22.04-ROS2)</font>

```plain
source ~/pika_ros/install/setup.sh
ros2 launch data_tools run_data_publish.launch.py type:=single_pika datasetDir:=$HOME/agilex/data/ episodeIndex:=0  # 单夹持器
ros2 launch data_tools run_data_publish.launch.py type:=multi_pika  datasetDir:=$HOME/agilex/data/ episodeIndex:=0  # 双夹持器
ros2 launch data_tools run_data_publish.launch.py type:=single_pika_teleop datasetDir:=$HOME/agilex/data/ episodeIndex:=0  # 单夹持器遥操作
ros2 launch data_tools run_data_publish.launch.py type:=multi_pika_teleop  datasetDir:=$HOME/agilex/data/ episodeIndex:=0  # 双夹持器遥操作
```

<font style="color:#333333;">若数据已经生成HDF5，也可采用以下命令以读取HDF5的方式进行数据重播。其中datasetDir参数为数据目录；episodeName 参数为需要重播的数据文件夹名称。</font>

```plain
cd ~/pika_ros/scripts
python3 data_publish.py --type single_pika --datasetDir $HOME/agilex/data/ --episodeName episode0  # 单夹持器
python3 data_publish.py --type multi_pika --datasetDir $HOME/agilex/data/ --episodeName episode0  # 双夹持器
python3 data_publish.py --type single_pika_teleop --datasetDir $HOME/agilex/data/ --episodeName episode0  # 单夹持器遥操作
python3 data_publish.py --type multi_pika_teleop --datasetDir $HOME/agilex/data/ --episodeName episode0  # 双夹持器遥操作
```

<font style="color:#333333;">重播的数据将以话题的形式重新发布，可以通过订阅话题进行查看。</font>

## **<font style="color:#1a1a1a;">7</font>****<font style="color:#1a1a1a;">.</font>****<font style="color:#1a1a1a;">4</font>****<font style="color:#1a1a1a;"> 数据加载</font>**
<font style="color:#333333;">在训练过程中加载数据</font>

<font style="color:#333333;">提供一个加载数据的示例，可以参照~/</font><font style="color:#333333;">pika_ros</font><font style="color:#333333;">/</font><font style="color:#333333;">scripts/load_data_example.py文件进行修改，运行以下命令测试加载数据。其中</font><font style="color:#333333;">datasetDir</font><font style="color:#333333;">参数为数据目录。</font>

```plain
python3 load_data_example.py --datasetDir $HOME/agilex/data/
```

# **<font style="color:#1a1a1a;">八</font>****<font style="color:#1a1a1a;">、常见问题处理</font>**
## **<font style="color:#1a1a1a;">8</font>****<font style="color:#1a1a1a;">.</font>****<font style="color:#1a1a1a;">1</font>****<font style="color:#1a1a1a;">日常维护指南</font>**
<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">基站日常清洁：</font>**

<font style="color:#333333;">请务必使基站及其电源适配器保持干燥并远离液体，以免造成电击伤害。按照如下步骤清洁基站：</font>

<font style="color:#333333;">●</font><font style="color:#333333;"> </font>**<font style="color:#333333;">清洁步骤：</font>**

<font style="color:#333333;">（1）拔下插头并拆下基站。</font>

<font style="color:#333333;">（2）使用蘸有少量水的非磨蚀性清洁布清洁基站。请勿使用清洁剂。清洁基站时，请勿刮擦前面板，也不要拆卸其任何部件。</font>

## **<font style="color:#1a1a1a;">8</font>****<font style="color:#1a1a1a;">.2</font>****<font style="color:#1a1a1a;">常见问题和解决方案</font>**
**<font style="color:#333333;">Q1: 在执行校准指令过程中，无法找到driver_openvr.so文件，出现如下报错</font>**<font style="color:#ff0000;">Error loading </font><font style="color:#ff0000;">	</font><font style="color:#ff0000;">/home/midea/liuxin/PIKA/pika ros/install/lib/plugins</font>

<font style="color:#ff0000;">/driver openvr.so: libopenvr api so.1: cannot open shared object</font>

<font style="color:#ff0000;">le: No such file or directory</font>

<font style="color:#333333;">安装依赖： </font><font style="color:#333333;">sudo apt install libopenvr-dev 后再次进行校准</font>

**<font style="color:#333333;">Q2: 校准时终端一直停留不动，并且没有显示定位误差</font>**

<font style="color:#333333;">	</font><font style="color:#333333;">rm ~/.config/libsurvive/config.json </font>

<font style="color:#333333;">	将</font><font style="color:#333333;">config.json 文件移除后再次进行校准</font>

**<font style="color:#333333;">Q3: 校准结束后显示有 error failures</font>**

<font style="color:#333333;">	</font><font style="color:#333333;">有 error failures 代表此次校准是失败的，检查当前环境是否有阳光照射或者当下环境 是否有主动发射红外光的设备。再次检查基站摆放位置，确保sense在基站的FOV内。当以上事项都检查完毕，再次运行校准程序。</font>

**<font style="color:#333333;">Q4: 当校准完成，使用一段时间后发现TF坐标飘了</font>**

<font style="color:#333333;">检查当前环境是否有阳光照射或者当下环境是否有主动发射红外光的设备。再次检查基站摆放位置，确保sense在基站的FOV内。当以上事项都检查完毕，再次运行校准程序。</font>

**<font style="color:#333333;">Q5: 相机通过编译后，能从realsense-viewer看到画面，但用ros启动的时候出现报错</font>**<font style="color:#ff0000;">/home/name/pika_ros/install/lib/librealsense2_camera.so: undefined symbol: _ZN20ddynamic_reconfigure19DDynamicReconfigureC1ERKN3ros10NodeHandleE</font>

<font style="color:#333333;">这个问题产生的原因是</font><font style="color:#333333;">ros-noetic-ddynamic-reconfigure该模块默认安装的是最新版本，由于</font><font style="color:#333333;">版本更新</font><font style="color:#333333;">，导致不可用。可用版本已放到pika_ros/source/下。名称为：ros-noetic-ddynamic-reconfigure_0.3.2-1focal.20240913.193805_amd64.deb，使用dpkg 安装即可：</font><font style="color:#333333;">sudo dpkg -i ros-noetic-ddynamic-reconfigure_0.3.2-1focal.20240913.193805_amd64.deb </font>

**<font style="color:#333333;">Q6: 位基站无法正常正常定位？</font>**

<font style="color:#333333;">检查基站摆放位置，基站供电，PIKA-Sense与Pika-Station之间是否有遮挡，是否存在红外干扰源。</font>

**<font style="color:#333333;">Q7: 鱼眼相机掉线？</font>**

<font style="color:#333333;">使用ubuntu自带的相机软件【茄子】，尝试打开鱼眼相机画面，如果仍获取不到图像，请联系我们的技术支持。</font>

**<font style="color:#333333;">Q8 :双目相机掉线</font>**

<font style="color:#333333;">	打开终端，输入 realsense-viewer 打开界面，看是否识别到相机，如没有，请联系我们的技术支持。</font>

**<font style="color:#333333;">Q9: 如果需要获取姿信息，读tf可以吗？</font>**

<font style="color:#333333;">如果是单个pika的话 位姿信息可以通过订阅 /pika_pose 来获取</font>

**<font style="color:#333333;">Q10:出现如下报错：Failed to Call service</font>**

<font style="color:#333333;">单独出现这个报错不需要处理，是采集的服务没有开</font>

**<font style="color:#333333;">Q11: 出现下图报错</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442592797-631898f7-47bf-45c2-8025-f0ab0db2bd22.png" width="580" title="" crop="0,0,1,1" id="ufba3f934" class="ne-image">

<font style="color:#333333;">没有给install目录加权限</font>

<font style="color:#333333;">chmod 777 -R install/</font>

**<font style="color:#333333;">Q12: bash scripts/start_</font>****<font style="color:#333333;">single_</font>****<font style="color:#333333;">sensor. bash报错，请问是可能什么问题？</font>**

[realsense2_camera(3).zip](https://drive.weixin.qq.com/s?k=AKcACgdBAAgOrfJWmLAXEA5gb3ANM)<font style="color:#333333;"> (可以右击另存为)</font><font style="color:#333333;">这个放到src目录下，使用 catkin_make install -DCATKIN_WHITELIST_PACKAGES="" 进行编译</font>

<font style="color:#333333;">Q13：出现如下报错</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1749442593586-4c34199d-e279-43e6-bea3-6f83ac70aff7.png" width="580" title="" crop="0,0,1,1" id="u8df2ebb2" class="ne-image">

```bash
Traceback (most recent call last):
  File "/home/ppn/miniconda3/envs/tv/lib/python3.8/site-packages/casadi/casadi.py", line 18, in swig_import_helper
    return importlib.import_module(mname)
  File "/home/ppn/miniconda3/envs/tv/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 657, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 556, in module_from_spec
  File "<frozen importlib._bootstrap_external>", line 1166, in create_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
ImportError: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/ppn/miniconda3/envs/tv/lib/python3.8/site-packages/casadi/_casadi.cpython-38-x86_64-linux-gnu.so)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "1.py", line 10, in <module>
    import casadi
  File "/home/ppn/miniconda3/envs/tv/lib/python3.8/site-packages/casadi/__init__.py", line 36, in <module>
    from casadi.casadi import *
  File "/home/ppn/miniconda3/envs/tv/lib/python3.8/site-packages/casadi/casadi.py", line 21, in <module>
    _casadi = swig_import_helper()
  File "/home/ppn/miniconda3/envs/tv/lib/python3.8/site-packages/casadi/casadi.py", line 20, in swig_import_helper
    return importlib.import_module('_casadi')
  File "/home/ppn/miniconda3/envs/tv/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ModuleNotFoundError: No module named '_casadi'
```

<font style="color:#333333;">这个问题的原因是程序在运行时，错误地链接了系统自带的、版本较旧的 C++ 标准库，而不是 conda 环境 中安装的、与 casadi 兼容的新版本库。通过设LD_PRELOAD=/home/ppn/miniconda3/envs/tv/lib/libstdc++.so.6，强制动态链接器优先加载了 conda 环境中的正确库文件，从而解决了版本不匹配导致的导入错误。 </font>

<font style="color:#333333;">根据实际的路径更改 export LD_PRELOAD=/home/<user name>/miniconda3/envs/pika/lib/libstdc++.so.6 </font>

# **<font style="color:#1a1a1a;">附录一：尺寸图纸</font>**
### **<font style="color:#1a1a1a;">Pika </font>****<font style="color:#1a1a1a;">Gripper</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442594447-87b75c47-ff11-4d42-b8f1-865f1ca22b33.jpeg" width="570" title="" crop="0,0,1,1" id="uebbfb68e" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/29291030/1752219313121-2705554b-0fcb-458d-86cf-2b92943cbb2f.png" width="1348.6666666666667" title="" crop="0,0,1,1" id="HVBgl" class="ne-image">

注：相机相对位置尺寸 SENSE 与 GRIPPER 一致

### **<font style="color:#1a1a1a;">Pika Sense </font>**
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442595306-c0ed5ab2-3412-4165-b916-0a99c95ded13.jpeg" width="556" title="" crop="0,0,1,1" id="u0d4594e4" class="ne-image">



### **<font style="color:#1a1a1a;">Pika Station(高度可调节)</font>**
<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/29291030/1749442595404-ac66e5d3-1924-45a8-be56-aa04acc0fc9d.jpeg" width="559" title="" crop="0,0,1,1" id="u33c4576e" class="ne-image">

# **<font style="color:#1a1a1a;">附录二：推荐配置方案</font>**
| <font style="color:#333333;">配置方案</font> | | <font style="color:#333333;">配置清单</font> | <font style="color:#333333;">适用场景</font> |
| --- | --- | --- | --- |
| <font style="color:#333333;">配置一</font> | <font style="color:#333333;">推荐配置</font> | <font style="color:#333333;">Pika Station X 2 </font><br/><font style="color:#333333;">Pika Sense X 1</font><br/><font style="color:#333333;">Pika Gripper X1</font><br/><font style="color:#333333;">Piper X 1</font> | <font style="color:#333333;">单臂Pick Place 以及操作场景，用单个数据采集器（Pika Sense）采集数据，然后使用执行器安装到机械臂进行数据的推理；其中数据采集保存的电脑/工控机需要自己提供，机械臂需要自备，进行模型推理的工控机或者算力卡需要</font><font style="color:#333333;">自行</font><font style="color:#333333;">配置；</font><br/><font style="color:#333333;">满足6*6M的作业空间覆盖；</font> |
| <font style="color:#333333;">配置二</font> | <font style="color:#333333;">常规配置</font> | <font style="color:#333333;">Pika Station X 2 </font><br/><font style="color:#333333;">Pika Sense X 2</font><br/><font style="color:#333333;">Pika Gripper X 2</font> | <font style="color:#333333;">双臂Pick Place 的复杂操作场景，使用两个数据采集进行双采集器（Pika Sense）同步采集数据，然后使用执行器安装到机械臂进行数据的推理；其中数据采集保存的电脑/工控机需要自己提供，机械臂需要自备，进行模型推理的工控机或者算力卡需要</font><font style="color:#333333;">自己</font><font style="color:#333333;">配置；</font><br/><font style="color:#333333;">预计可满足5*5M的作业空间覆盖；</font> |
| <font style="color:#333333;">配置三</font> | <font style="color:#333333;">大空间配置</font> | <font style="color:#333333;">Pika Station X 4 </font><br/><font style="color:#333333;">Pika Sense X 2</font><br/><font style="color:#333333;">Pika Gripper X 2</font> | <font style="color:#333333;">双臂Pick Place 的复杂操作场景，使用两个数据采集进行双采集器（Pika Sense）同步采集数据，然后使用执行器安装到机械臂进行数据的推理；其中数据采集保存的电脑/工控机需要自己提供，机械臂需要自备，进行模型推理的工控机或者算力卡需要</font><font style="color:#333333;">自己</font><font style="color:#333333;">配置；</font><br/><font style="color:#333333;">预计可满足10*10M的作业空间覆盖；</font> |


