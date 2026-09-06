<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FuNing Hospital 综合管理系统</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        @media print {
            .no-print {display: none !important;}
            .print-area {width: 100% !important;}
        }
        .tab-content{margin-top:15px;}
    </style>
</head>
<body class="bg-light">
<div class="container py-4">
    <h2 class="text-center mb-4">🏥 医院综合管理系统</h2>

    <ul class="nav nav-tabs mb-3" id="mainTab">
        <li class="nav-item">
            <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#caseTab">病例管理</button>
        </li>
        <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#inHospitalTab">住院管理</button>
        </li>
        <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#docTab">门诊文书生成</button>
        </li>
        <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#deathReportTab">死亡报告</button>
        </li>
        <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#operationTab">手术记录</button>
        </li>
    </ul>

    <div class="tab-content">
        <!--病例管理-->
        <div class="tab-pane fade show active" id="caseTab">
            <div class="row mb-3">
                <div class="col-md-6">
                    <input type="text" id="searchInput" class="form-control" placeholder="输入患者姓名/病历号搜索">
                </div>
                <div class="col-md-2">
                    <button class="btn btn-primary w-100" data-bs-toggle="modal" data-bs-target="#caseModal">新增病例</button>
                </div>
            </div>
            <div class="card shadow">
                <div class="card-body">
                    <table class="table table-hover table-striped">
                        <thead>
                        <tr>
                            <th>病历编号</th>
                            <th>患者姓名</th>
                            <th>性别</th>
                            <th>年龄</th>
                            <th>诊断</th>
                            <th>就诊日期</th>
                            <th>操作</th>
                        </tr>
                        </thead>
                        <tbody id="caseTableBody"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!--住院管理-->
        <div class="tab-pane fade" id="inHospitalTab">
            <div class="row mb-3">
                <div class="col-md-6">
                    <input type="text" id="hospitalSearchInput" class="form-control" placeholder="姓名/住院号搜索">
                </div>
                <div class="col-md-2">
                    <button class="btn btn-success w-100" data-bs-toggle="modal" data-bs-target="#hospitalModal">新增住院登记</button>
                </div>
            </div>
            <div class="card shadow">
                <div class="card-body">
                    <table class="table table-hover table-striped">
                        <thead>
                        <tr>
                            <th>住院编号</th>
                            <th>患者姓名</th>
                            <th>床位号</th>
                            <th>入院日期</th>
                            <th>病情摘要</th>
                            <th>住院状态</th>
                            <th>操作</th>
                        </tr>
                        </thead>
                        <tbody id="hospitalTableBody"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!--门诊文书-->
        <div class="tab-pane fade" id="docTab">
            <div class="row mb-3">
                <div class="col-md-6">
                    <input type="text" id="docSearchInput" class="form-control" placeholder="患者姓名/文书编号搜索">
                </div>
                <div class="col-md-2">
                    <button class="btn btn-dark w-100" data-bs-toggle="modal" data-bs-target="#docModal">新建门诊文书</button>
                </div>
            </div>
            <div class="card shadow">
                <div class="card-body">
                    <table class="table table-hover table-striped">
                        <thead>
                        <tr>
                            <th>文书编号</th>
                            <th>患者姓名</th>
                            <th>就诊日期</th>
                            <th>诊断</th>
                            <th>操作</th>
                        </tr>
                        </thead>
                        <tbody id="docTableBody"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!--死亡报告-->
        <div class="tab-pane fade" id="deathReportTab">
            <div class="row mb-3">
                <div class="col-md-6">
                    <input type="text" id="deathSearchInput" class="form-control" placeholder="死者姓名/报告编号搜索">
                </div>
                <div class="col-md-2">
                    <button class="btn btn-danger w-100" data-bs-toggle="modal" data-bs-target="#deathModal">新建死亡报告</button>
                </div>
            </div>
            <div class="card shadow">
                <div class="card-body">
                    <table class="table table-hover table-striped">
                        <thead>
                        <tr>
                            <th>报告编号</th>
                            <th>死者姓名</th>
                            <th>性别</th>
                            <th>年龄</th>
                            <th>死亡时间</th>
                            <th>主要死亡原因</th>
                            <th>操作</th>
                        </tr>
                        </thead>
                        <tbody id="deathTableBody"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!--手术记录模块-->
        <div class="tab-pane fade" id="operationTab">
            <div class="row mb-3">
                <div class="col-md-6">
                    <input type="text" id="opSearchInput" class="form-control" placeholder="患者姓名/手术编号搜索">
                </div>
                <div class="col-md-2">
                    <button class="btn btn-warning w-100 text-dark" data-bs-toggle="modal" data-bs-target="#operationModal">新建手术记录</button>
                </div>
            </div>
            <div class="card shadow">
                <div class="card-body">
                    <table class="table table-hover table-striped">
                        <thead>
                        <tr>
                            <th>手术编号</th>
                            <th>患者姓名</th>
                            <th>手术名称</th>
                            <th>手术时间</th>
                            <th>手术状态</th>
                            <th>主刀医师</th>
                            <th>操作</th>
                        </tr>
                        </thead>
                        <tbody id="operationTableBody"></tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<!--病例弹窗-->
<div class="modal fade" id="caseModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">病例信息/h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="hidden" id="editId">
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>病历编号</label>
                        <input type="text" id="caseNo" class="form-control" required>
                    </div>
                    <div class="col-md-6">
                        <label>患者姓名</label>
                        <input type="text" id="patientName" class="form-control" required>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>性别</label>
                        <select id="gender" class="form-select">
                            <option value="男">男</option>
                            <option value="女">女</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label>年龄</label>
                        <input type="number" id="age" class="form-control">
                    </div>
                </div>
                <div class="mb-2">
                    <label>诊断结果</label>
                    <input type="text" id="diagnosis" class="form-control">
                </div>
                <div class="mb-2">
                    <label>就诊日期</label>
                    <input type="date" id="visitDate" class="form-control">
                </div>
                <div class="mb-2">
                    <label>主诉与病史</label>
                    <textarea id="content" class="form-control" rows="3"></textarea>
                </div>
                <div class="mb-2">
                    <label>病例照片</label>
                    <input type="file" id="photoInput" class="form-control" accept="image/*">
                    <div id="photoPreviewBox" class="mt-2"></div>
                </div>
                <div class="border p-3 rounded mt-3">
                    <h6>💊 处方开药</h6>
                    <div class="row mb-2">
                        <div class="col-md-4">
                            <input type="text" id="drugName" class="form-control" placeholder="药品名称">
                        </div>
                        <div class="col-md-3">
                            <input type="text" id="drugDosage" class="form-control" placeholder="剂量">
                        </div>
                        <div class="col-md-3">
                            <input type="text" id="drugUsage" class="form-control" placeholder="用法">
                        </div>
                        <div class="col-md-2">
                            <button type="button" id="addDrugBtn" class="btn btn-success w-100">添加</button>
                        </div>
                    </div>
                    <div id="drugListBox"></div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                <button class="btn btn-success" id="saveBtn">保存</button>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="detailModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">病例详情</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body" id="detailBody"></div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
            </div>
        </div>
    </div>
</div>

<!--住院弹窗-->
<div class="modal fade" id="hospitalModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">住院登记</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="hidden" id="hospitalEditId">
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>住院编号</label>
                        <input type="text" id="hospitalNo" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label>患者姓名</label>
                        <input type="text" id="hospitalPatient" class="form-control">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>床位号</label>
                        <input type="text" id="bedNo" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label>入院日期</label>
                        <input type="date" id="inDate" class="form-control">
                    </div>
                </div>
                <div class="mb-2">
                    <label>病情摘要</label>
                    <textarea id="illnessDesc" class="form-control" rows="3"></textarea>
                </div>
                <div class="mb-2">
                    <label>住院状态</label>
                    <select id="hospitalStatus" class="form-select">
                        <option value="住院中">住院中</option>
                        <option value="已出院">已出院</option>
                    </select>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                <button class="btn btn-primary" id="saveHospitalBtn">保存住院信息</button>
            </div>
        </div>
    </div>
</div>

<!--门诊文书弹窗-->
<div class="modal fade" id="docModal" tabindex="-1">
    <div class="modal-dialog modal-xl">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">📄 门诊病历文书编辑</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="hidden" id="docEditId">
                <div class="row mb-2">
                    <div class="col-md-4">
                        <label>文书编号</label>
                        <input type="text" id="docNo" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>患者姓名</label>
                        <input type="text" id="docName" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>就诊日期</label>
                        <input type="date" id="docDate" class="form-control">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>性别</label>
                        <input type="text" id="docSex" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label>年龄</label>
                        <input type="text" id="docAge" class="form-control">
                    </div>
                </div>
                <div class="mb-2">
                    <label>主诉</label>
                    <textarea id="docZhuSu" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>现病史</label>
                    <textarea id="docXianBingShi" class="form-control" rows="3"></textarea>
                </div>
                <div class="mb-2">
                    <label>既往史</label>
                    <textarea id="docJiWangShi" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>体格检查</label>
                    <textarea id="docTiJian" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>辅助检查</label>
                    <textarea id="docFuJian" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>初步诊断</label>
                    <textarea id="docZhenDuan" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>处理意见 / 医嘱</label>
                    <textarea id="docYiZhu" class="form-control" rows="3"></textarea>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                <button class="btn btn-success" id="saveDocBtn">保存文书</button>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="printDocModal" tabindex="-1">
    <div class="modal-dialog modal-xl">
        <div class="modal-content">
            <div class="modal-header no-print">
                <h5 class="modal-title">📑 门诊病历文书</h5>
                <button class="btn btn-primary" onclick="window.print()">🖨️ 打印文书</button>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body print-area" id="printContent"></div>
        </div>
    </div>
</div>

<!--死亡报告弹窗-->
<div class="modal fade" id="deathModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">☠️ 死亡报告（枫叶医院RP）</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="hidden" id="deathEditId">
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>报告编号</label>
                        <input type="text" id="deathReportNo" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label>死者姓名</label>
                        <input type="text" id="deathName" class="form-control">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>性别</label>
                        <select id="deathGender" class="form-select">
                            <option value="男">男</option>
                            <option value="女">女</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label>年龄</label>
                        <input type="number" id="deathAge" class="form-control">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>入院编号（住院号）</label>
                        <input type="text" id="deathInNo" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label>死亡时间</label>
                        <input type="datetime-local" id="deathTime" class="form-control">
                    </div>
                </div>
                <div class="mb-2">
                    <label>主要死亡原因</label>
                    <input type="text" id="deathMainReason" class="form-control" placeholder="例如：重度创伤、失血性休克、多器官衰竭">
                </div>
                <div class="mb-2">
                    <label>其他并发症</label>
                    <textarea id="deathOtherIll" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>抢救经过（RP剧情描述）</label>
                    <textarea id="deathRescueProcess" class="form-control" rows="4" placeholder="记录抢救过程，用于Roblox角色扮演"></textarea>
                </div>
                <div class="mb-2">
                    <label>遗体处置</label>
                    <input type="text" id="deathBodyDeal" class="form-control" placeholder="转殡仪馆 / 家属领回">
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>开具报告医师</label>
                        <input type="text" id="deathDoctor" class="form-control">
                    </div>
                    <div class="col-md-6">
                        <label>报告开具日期</label>
                        <input type="date" id="deathMakeDate" class="form-control">
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                <button class="btn btn-danger" id="saveDeathBtn">保存死亡报告</button>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="deathPrintModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header no-print">
                <h5 class="modal-title">📋死亡报告（可复制用于Roblox枫叶医院RP）</h5>
                <button class="btn btn-primary" onclick="window.print()">🖨打印</button>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body print-area" id="deathPrintBody"></div>
        </div>
    </div>
</div>

<!--手术记录弹窗-->
<div class="modal fade" id="operationModal" tabindex="-1">
    <div class="modal-dialog modal-xl">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">🏥 手术记录 & 手术通知书</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <input type="hidden" id="opEditId">
                <div class="row mb-2">
                    <div class="col-md-4">
                        <label>手术编号</label>
                        <input type="text" id="opNo" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>患者姓名</label>
                        <input type="text" id="opPatientName" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>住院号</label>
                        <input type="text" id="opHospitalNo" class="form-control">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-4">
                        <label>性别</label>
                        <select id="opGender" class="form-select">
                            <option value="男">男</option>
                            <option value="女">女</option>
                        </select>
                    </div>
                    <div class="col-md-4">
                        <label>年龄</label>
                        <input type="number" id="opAge" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>手术状态</label>
                        <select id="opStatus" class="form-select">
                            <option value="待手术">待手术</option>
                            <option value="手术中">手术中</option>
                            <option value="手术完成">手术完成</option>
                            <option value="手术取消">手术取消</option>
                        </select>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-6">
                        <label>手术名称</label>
                        <input type="text" id="opName" class="form-control" placeholder="例如：腹腔探查术、创伤清创缝合术">
                    </div>
                    <div class="col-md-6">
                        <label>麻醉方式</label>
                        <input type="text" id="opAnaesthesia" class="form-control" placeholder="全麻/半麻/局部麻醉">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-4">
                        <label>手术开始时间</label>
                        <input type="datetime-local" id="opStartTime" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>手术结束时间</label>
                        <input type="datetime-local" id="opEndTime" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>术中出血量(ml)</label>
                        <input type="text" id="opBleed" class="form-control">
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-md-4">
                        <label>主刀医师</label>
                        <input type="text" id="opSurgeon" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>手术助手</label>
                        <input type="text" id="opAssistant" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>器械护士</label>
                        <input type="text" id="opNurse" class="form-control">
                    </div>
                </div>
                <div class="mb-2">
                    <label>术前诊断</label>
                    <textarea id="opPreDiagnosis" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>术后诊断</label>
                    <textarea id="opPostDiagnosis" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>手术经过（RP剧情）</label>
                    <textarea id="opProcess" class="form-control" rows="4" placeholder="记录手术全过程，用于Roblox角色扮演"></textarea>
                </div>
                <div class="mb-2">
                    <label>术中情况与并发症</label>
                    <textarea id="opComplication" class="form-control" rows="2"></textarea>
                </div>
                <div class="mb-2">
                    <label>术后注意事项/医嘱</label>
                    <textarea id="opAdvice" class="form-control" rows="2"></textarea>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                <button class="btn btn-warning text-dark" id="saveOpBtn">保存手术记录</button>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="opPrintModal" tabindex="-1">
    <div class="modal-dialog modal-xl">
        <div class="modal-content">
            <div class="modal-header no-print">
                <h5 class="modal-title">📑手术记录+手术通知书（枫叶医院RP）</h5>
                <button class="btn btn-primary" onclick="window.print()">🖨打印</button>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body print-area" id="opPrintBody"></div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
let tempPhotoBase64 = "";
let tempDrugList = [];

//本地存储读写
function getCaseList(){return JSON.parse(localStorage.getItem("caseList"))||[];}
function saveCaseList(d){localStorage.setItem("caseList",JSON.stringify(d));}

function getHospitalList(){return JSON.parse(localStorage.getItem("hospitalList"))||[];}
function saveHospitalList(d){localStorage.setItem("hospitalList",JSON.stringify(d));}

function getDocList(){return JSON.parse(localStorage.getItem("docList"))||[];}
function saveDocList(d){localStorage.setItem("docList",JSON.stringify(d));}

function getDeathList(){return JSON.parse(localStorage.getItem("deathReportList"))||[];}
function saveDeathList(d){localStorage.setItem("deathReportList",JSON.stringify(d));}

function getOpList(){return JSON.parse(localStorage.getItem("operationList"))||[];}
function saveOpList(d){localStorage.setItem("operationList",JSON.stringify(d));}

//========病例模块========
function renderTable(k=""){
    let list = getCaseList().filter(x=>!k||x.caseNo.includes(k)||x.patientName.includes(k));
    let t = document.getElementById("caseTableBody");
    t.innerHTML="";
    list.forEach(item=>{
        t.innerHTML+=`<tr>
            <td>${item.caseNo}</td>
            <td>${item.patientName}</td>
            <td>${item.gender}</td>
            <td>${item.age}</td>
            <td>${item.diagnosis}</td>
            <td>${item.visitDate}</td>
            <td>
                <button class="btn btn-sm btn-primary detail-btn" data-id="${item.id}">详情</button>
                <button class="btn btn-sm btn-info edit-btn" data-id="${item.id}">编辑</button>
                <button class="btn btn-sm btn-danger del-btn" data-id="${item.id}">删除</button>
            </td>
        </tr>`;
    })
}

document.getElementById("photoInput").onchange=function(e){
    let f=e.target.files[0];if(!f)return;
    let r=new FileReader();
    r.onload=ev=>{
        tempPhotoBase64=ev.target.result;
        document.getElementById("photoPreviewBox").innerHTML=`<img src="${tempPhotoBase64}" style="max-width:220px;" class="img-thumbnail">`;
    }
    r.readAsDataURL(f);
}

document.getElementById("addDrugBtn").onclick=function(){
    let n=document.getElementById("drugName").value.trim();
    let d=document.getElementById("drugDosage").value.trim();
    let u=document.getElementById("drugUsage").value.trim();
    if(!n)return alert("请输入药品名称");
    tempDrugList.push({name:n,dosage:d,usage:u});
    renderTempDrug();
    document.getElementById("drugName").value="";
    document.getElementById("drugDosage").value="";
    document.getElementById("drugUsage").value="";
}
function renderTempDrug(){
    let b=document.getElementById("drugListBox");b.innerHTML="";
    tempDrugList.forEach((x,i)=>{
        b.innerHTML+=`<div class="d-flex justify-content-between bg-light p-2 rounded mb-1">
            <span>${x.name} ${x.dosage} ${x.usage}</span>
            <button class="btn btn-sm btn-outline-danger del-drug" data-i="${i}">删除</button>
        </div>`;
    })
}
document.getElementById("drugListBox").onclick=e=>{
    if(e.target.classList.contains("del-drug")){
        tempDrugList.splice(e.target.dataset.i,1);
        renderTempDrug();
    }
}

document.getElementById("saveBtn").onclick=function(){
    let eid=document.getElementById("editId").value;
    let d={
        id:eid||Date.now()+"",
        caseNo:document.getElementById("caseNo").value.trim(),
        patientName:document.getElementById("patientName").value.trim(),
        gender:document.getElementById("gender").value,
        age:document.getElementById("age").value,
        diagnosis:document.getElementById("diagnosis").value.trim(),
        visitDate:document.getElementById("visitDate").value,
        content:document.getElementById("content").value.trim(),
        photo:tempPhotoBase64,
        drugs:[...tempDrugList]
    };
    if(!d.caseNo||!d.patientName)return alert("必填项不能为空");
    let arr=getCaseList();
    eid?arr[arr.findIndex(x=>x.id===eid)]=d:arr.push(d);
    saveCaseList(arr);
    bootstrap.Modal.getInstance(document.getElementById("caseModal")).hide();
    clearForm();renderTable();
}
function clearForm(){
    document.getElementById("editId").value="";
    document.getElementById("caseNo").value="";
    document.getElementById("patientName").value="";
    document.getElementById("gender").value="男";
    document.getElementById("age").value="";
    document.getElementById("diagnosis").value="";
    document.getElementById("visitDate").value="";
    document.getElementById("content").value="";
    document.getElementById("photoInput").value="";
    document.getElementById("photoPreviewBox").innerHTML="";
    tempPhotoBase64="";tempDrugList=[];renderTempDrug();
}

document.getElementById("caseTableBody").onclick=e=>{
    let id=e.target.dataset.id;if(!id)return;
    let list=getCaseList();
    if(e.target.classList.contains("del-btn")){
        if(confirm("删除？"))saveCaseList(list.filter(x=>x.id!==id)),renderTable();
    }else if(e.target.classList.contains("edit-btn")){
        let item=list.find(x=>x.id===id);
        document.getElementById("editId").value=item.id;
        document.getElementById("caseNo").value=item.caseNo;
        document.getElementById("patientName").value=item.patientName;
        document.getElementById("gender").value=item.gender;
        document.getElementById("age").value=item.age;
        document.getElementById("diagnosis").value=item.diagnosis;
        document.getElementById("visitDate").value=item.visitDate;
        document.getElementById("content").value=item.content;
        tempPhotoBase64=item.photo||"";
        document.getElementById("photoPreviewBox").innerHTML=tempPhotoBase64?`<img src="${tempPhotoBase64}" style="max-width:220px;" class="img-thumbnail">`:"";
        tempDrugList=item.drugs||[];renderTempDrug();
        new bootstrap.Modal(document.getElementById("caseModal")).show();
    }else if(e.target.classList.contains("detail-btn")){
        let item=list.find(x=>x.id===id);
        let p=item.photo?`<img src="${item.photo}" style="max-width:350px" class="img-fluid">`:"无照片";
        let drug="";
        if(item.drugs&&item.drugs.length>0){
            drug="<table class='table'><tr><td>药品</td><td>剂量</td><td>用法</td></tr>";
            item.drugs.forEach(x=>drug+=`<tr><td>${x.name}</td><td>${x.dosage}</td><td>${x.usage}</td></tr>`);
            drug+="</table>";
        }else drug="无处方";
        document.getElementById("detailBody").innerHTML=`
            <p><b>病历号：</b>${item.caseNo}</p>
            <p><b>姓名：</b>${item.patientName} ${item.gender} ${item.age}岁</p>
            <p><b>诊断：</b>${item.diagnosis}</p>
            <p><b>就诊日期：</b>${item.visitDate}</p>
            <p><b>病史：</b>${item.content||"无"}</p>
            <p><b>检查照片：</b>${p}</p>
            <p><b>处方药品：</b>${drug}</p>
        `;
        new bootstrap.Modal(document.getElementById("detailModal")).show();
    }
}
document.getElementById("searchInput").oninput=e=>renderTable(e.target.value.trim());
document.getElementById("caseModal").addEventListener("hidden.bs.modal",clearForm);

//========住院模块========
function renderHospitalTable(k=""){
    let list=getHospitalList().filter(x=>!k||x.hospitalNo.includes(k)||x.patientName.includes(k));
    let t=document.getElementById("hospitalTableBody");t.innerHTML="";
    list.forEach(item=>{
        let s=item.status=="住院中"?"bg-warning":"bg-success text-white";
        t.innerHTML+=`<tr>
            <td>${item.hospitalNo}</td>
            <td>${item.patientName}</td>
            <td>${item.bedNo}</td>
            <td>${item.inDate}</td>
            <td>${item.illnessDesc}</td>
            <td><span class="badge ${s}">${item.status}</span></td>
            <td>
                <button class="btn btn-sm btn-info hospital-edit" data-hid="${item.id}">编辑</button>
                <button class="btn btn-sm btn-outline-secondary hospital-out" data-hid="${item.id}">办理出院</button>
                <button class="btn btn-sm btn-danger hospital-del" data-hid="${item.id}">删除</button>
            </td>
        </tr>`;
    })
}
document.getElementById("saveHospitalBtn").onclick=function(){
    let hid=document.getElementById("hospitalEditId").value;
    let d={
        id:hid||Date.now()+"",
        hospitalNo:document.getElementById("hospitalNo").value.trim(),
        patientName:document.getElementById("hospitalPatient").value.trim(),
        bedNo:document.getElementById("bedNo").value.trim(),
        inDate:document.getElementById("inDate").value,
        illnessDesc:document.getElementById("illnessDesc").value.trim(),
        status:document.getElementById("hospitalStatus").value
    };
    if(!d.hospitalNo||!d.patientName)return alert("必填项不能为空");
    let arr=getHospitalList();
    hid?arr[arr.findIndex(x=>x.id===hid)]=d:arr.push(d);
    saveHospitalList(arr);
    bootstrap.Modal.getInstance(document.getElementById("hospitalModal")).hide();
    clearHospitalForm();renderHospitalTable();
}
function clearHospitalForm(){
    document.getElementById("hospitalEditId").value="";
    document.getElementById("hospitalNo").value="";
    document.getElementById("hospitalPatient").value="";
    document.getElementById("bedNo").value="";
    document.getElementById("inDate").value="";
    document.getElementById("illnessDesc").value="";
    document.getElementById("hospitalStatus").value="住院中";
}
document.getElementById("hospitalTableBody").onclick=e=>{
    let hid=e.target.dataset.hid;if(!hid)return;
    let list=getHospitalList();
    if(e.target.classList.contains("hospital-del")){
        if(confirm("删除？"))saveHospitalList(list.filter(x=>x.id!==hid)),renderHospitalTable();
    }else if(e.target.classList.contains("hospital-edit")){
        let item=list.find(x=>x.id===hid);
        document.getElementById("hospitalEditId").value=item.id;
        document.getElementById("hospitalNo").value=item.hospitalNo;
        document.getElementById("hospitalPatient").value=item.patientName;
        document.getElementById("bedNo").value=item.bedNo;
        document.getElementById("inDate").value=item.inDate;
        document.getElementById("illnessDesc").value=item.illnessDesc;
        document.getElementById("hospitalStatus").value=item.status;
        new bootstrap.Modal(document.getElementById("hospitalModal")).show();
    }else if(e.target.classList.contains("hospital-out")){
        let idx=list.findIndex(x=>x.id===hid);
        list[idx].status="已出院";
        saveHospitalList(list);renderHospitalTable();
    }
}
document.getElementById("hospitalSearchInput").oninput=e=>renderHospitalTable(e.target.value.trim());
document.getElementById("hospitalModal").addEventListener("hidden.bs.modal",clearHospitalForm);

//========门诊文书========
function renderDocTable(k=""){
    let list=getDocList().filter(x=>!k||x.docNo.includes(k)||x.name.includes(k));
    let t=document.getElementById("docTableBody");t.innerHTML="";
    list.forEach(item=>{
        t.innerHTML+=`<tr>
            <td>${item.docNo}</td>
            <td>${item.name}</td>
            <td>${item.date}</td>
            <td>${item.zd}</td>
            <td>
                <button class="btn btn-sm btn-dark doc-print" data-did="${item.id}">打印预览</button>
                <button class="btn btn-sm btn-info doc-edit" data-did="${item.id}">编辑</button>
                <button class="btn btn-sm btn-danger doc-del" data-did="${item.id}">删除</button>
            </td>
        </tr>`;
    })
}

document.getElementById("saveDocBtn").onclick=function(){
    let did=document.getElementById("docEditId").value;
    let d={
        id:did||Date.now()+"",
        docNo:document.getElementById("docNo").value.trim(),
        name:document.getElementById("docName").value.trim(),
        date:document.getElementById("docDate").value,
        sex:document.getElementById("docSex").value.trim(),
        age:document.getElementById("docAge").value.trim(),
        zs:document.getElementById("docZhuSu").value.trim(),
        xbs:document.getElementById("docXianBingShi").value.trim(),
        jws:document.getElementById("docJiWangShi").value.trim(),
        tj:document.getElementById("docTiJian").value.trim(),
        fj:document.getElementById("docFuJian").value.trim(),
        zd:document.getElementById("docZhenDuan").value.trim(),
        yz:document.getElementById("docYiZhu").value.trim()
    };
    if(!d.docNo||!d.name)return alert("文书编号、患者姓名不能为空！");
    let arr=getDocList();
    did?arr[arr.findIndex(x=>x.id===did)]=d:arr.push(d);
    saveDocList(arr);
    bootstrap.Modal.getInstance(document.getElementById("docModal")).hide();
    clearDocForm();renderDocTable();
}

function clearDocForm(){
    document.getElementById("docEditId").value="";
    document.getElementById("docNo").value="";
    document.getElementById("docName").value="";
    document.getElementById("docDate").value="";
    document.getElementById("docSex").value="";
    document.getElementById("docAge").value="";
    document.getElementById("docZhuSu").value="";
    document.getElementById("docXianBingShi").value="";
    document.getElementById("docJiWangShi").value="";
    document.getElementById("docTiJian").value="";
    document.getElementById("docFuJian").value="";
    document.getElementById("docZhenDuan").value="";
    document.getElementById("docYiZhu").value="";
}

document.getElementById("docTableBody").onclick=e=>{
    let did=e.target.dataset.did;if(!did)return;
    let list=getDocList();
    let item=list.find(x=>x.id===did);
    if(e.target.classList.contains("doc-del")){
        if(confirm("删除文书？"))saveDocList(list.filter(x=>x.id!==did)),renderDocTable();
    }else if(e.target.classList.contains("doc-edit")){
        document.getElementById("docEditId").value=item.id;
        document.getElementById("docNo").value=item.docNo;
        document.getElementById("docName").value=item.name;
        document.getElementById("docDate").value=item.date;
        document.getElementById("docSex").value=item.sex;
        document.getElementById("docAge").value=item.age;
        document.getElementById("docZhuSu").value=item.zs;
        document.getElementById("docXianBingShi").value=item.xbs;
        document.getElementById("docJiWangShi").value=item.jws;
        document.getElementById("docTiJian").value=item.tj;
        document.getElementById("docFuJian").value=item.fj;
        document.getElementById("docZhenDuan").value=item.zd;
        document.getElementById("docYiZhu").value=item.yz;
        new bootstrap.Modal(document.getElementById("docModal")).show();
    }else if(e.target.classList.contains("doc-print")){
        document.getElementById("printContent").innerHTML=`
        <div class="p-4">
            <h4 class="text-center">门 诊 病 历 文 书</h4>
            <hr>
            <p><strong>文书编号：</strong>${item.docNo}</p>
            <p><strong>患者姓名：</strong>${item.name} &nbsp;&nbsp; <strong>性别：</strong>${item.sex} &nbsp;&nbsp; <strong>年龄：</strong>${item.age}岁</p>
            <p><strong>就诊日期：</strong>${item.date}</p>
            <p><strong>主诉：</strong>${item.zs||"无"}</p>
            <p><strong>现病史：</strong>${item.xbs||"无"}</p>
            <p><strong>既往史：</strong>${item.jws||"无"}</p>
            <p><strong>体格检查：</strong>${item.tj||"无"}</p>
            <p><strong>辅助检查：</strong>${item.fj||"无"}</p>
            <p><strong>初步诊断：</strong>${item.zd||"无"}</p>
            <p><strong>医嘱与处理意见：</strong>${item.yz||"无"}</p>
            <hr>
            <p class="text-end">医师签名：___________ &nbsp;&nbsp; 日期：___________</p>
        </div>`;
        new bootstrap.Modal(document.getElementById("printDocModal")).show();
    }
}

document.getElementById("docSearchInput").oninput=e=>renderDocTable(e.target.value.trim());
document.getElementById("docModal").addEventListener("hidden.bs.modal",clearDocForm);

//========死亡报告模块========
function renderDeathTable(k=""){
    let list=getDeathList().filter(x=>!k||x.reportNo.includes(k)||x.name.includes(k));
    let t=document.getElementById("deathTableBody");t.innerHTML="";
    list.forEach(item=>{
        t.innerHTML+=`<tr>
            <td>${item.reportNo}</td>
            <td>${item.name}</td>
            <td>${item.gender}</td>
            <td>${item.age}</td>
            <td>${item.deathTime||""}</td>
            <td>${item.mainReason}</td>
            <td>
                <button class="btn btn-sm btn-danger death-print" data-deid="${item.id}">RP打印预览</button>
                <button class="btn btn-sm btn-info death-edit" data-deid="${item.id}">编辑</button>
                <button class="btn btn-sm btn-outline-danger death-del" data-deid="${item.id}">删除</button>
            </td>
        </tr>`;
    })
}

document.getElementById("saveDeathBtn").onclick=function(){
    let deid=document.getElementById("deathEditId").value;
    let d={
        id:deid||Date.now()+"",
        reportNo:document.getElementById("deathReportNo").value.trim(),
        name:document.getElementById("deathName").value.trim(),
        gender:document.getElementById("deathGender").value,
        age:document.getElementById("deathAge").value,
        inNo:document.getElementById("deathInNo").value.trim(),
        deathTime:document.getElementById("deathTime").value,
        mainReason:document.getElementById("deathMainReason").value.trim(),
        otherIll:document.getElementById("deathOtherIll").value.trim(),
        rescueProcess:document.getElementById("deathRescueProcess").value.trim(),
        bodyDeal:document.getElementById("deathBodyDeal").value.trim(),
        doctor:document.getElementById("deathDoctor").value.trim(),
        makeDate:document.getElementById("deathMakeDate").value
    };
    if(!d.reportNo||!d.name)return alert("报告编号、死者姓名不能为空！");
    let arr=getDeathList();
    deid?arr[arr.findIndex(x=>x.id===deid)]=d:arr.push(d);
    saveDeathList(arr);
    bootstrap.Modal.getInstance(document.getElementById("deathModal")).hide();
    clearDeathForm();renderDeathTable();
}

function clearDeathForm(){
    document.getElementById("deathEditId").value="";
    document.getElementById("deathReportNo").value="";
    document.getElementById("deathName").value="";
    document.getElementById("deathGender").value="男";
    document.getElementById("deathAge").value="";
    document.getElementById("deathInNo").value="";
    document.getElementById("deathTime").value="";
    document.getElementById("deathMainReason").value="";
    document.getElementById("deathOtherIll").value="";
    document.getElementById("deathRescueProcess").value="";
    document.getElementById("deathBodyDeal").value="";
    document.getElementById("deathDoctor").value="";
    document.getElementById("deathMakeDate").value="";
}

document.getElementById("deathTableBody").onclick=e=>{
    let deid=e.target.dataset.deid;if(!deid)return;
    let list=getDeathList();
    let item=list.find(x=>x.id===deid);
    if(e.target.classList.contains("death-del")){
        if(confirm("确定删除这份死亡报告？"))saveDeathList(list.filter(x=>x.id!==deid)),renderDeathTable();
    }else if(e.target.classList.contains("death-edit")){
        document.getElementById("deathEditId").value=item.id;
        document.getElementById("deathReportNo").value=item.reportNo;
        document.getElementById("deathName").value=item.name;
        document.getElementById("deathGender").value=item.gender;
        document.getElementById("deathAge").value=item.age;
        document.getElementById("deathInNo").value=item.inNo;
        document.getElementById("deathTime").value=item.deathTime;
        document.getElementById("deathMainReason").value=item.mainReason;
        document.getElementById("deathOtherIll").value=item.otherIll;
        document.getElementById("deathRescueProcess").value=item.rescueProcess;
        document.getElementById("deathBodyDeal").value=item.bodyDeal;
        document.getElementById("deathDoctor").value=item.doctor;
        document.getElementById("deathMakeDate").value=item.makeDate;
        new bootstrap.Modal(document.getElementById("deathModal")).show();
    }else if(e.target.classList.contains("death-print")){
        document.getElementById("deathPrintBody").innerHTML=`
        <div class="p-4">
            <h4 class="text-center">死 亡 报 告</h4>
            <hr>
            <p><strong>报告编号：</strong>${item.reportNo}</p>
            <p><strong>死者姓名：</strong>${item.name} &nbsp;&nbsp;性别：${item.gender} &nbsp;&nbsp;年龄：${item.age}</p>
            <p><strong>住院号：</strong>${item.inNo||"无"}</p>
            <p><strong>死亡时间：</strong>${item.deathTime||""}</p>
            <p><strong>主要死亡原因：</strong>${item.mainReason}</p>
            <p><strong>其他并发症：</strong>${item.otherIll||"无"}</p>
            <p><strong>抢救经过：</strong>${item.rescueProcess||"无记录"}</p>
            <p><strong>遗体处置：</strong>${item.bodyDeal||"无"}</p>
            <hr>
            <p><strong>开具医师：</strong>${item.doctor||""}</p>
            <p><strong>报告开具日期：</strong>${item.makeDate||""}</p>
            <p class="text-end">医师签字：_______________</p>
        </div>`;
        new bootstrap.Modal(document.getElementById("deathPrintModal")).show();
    }
}
document.getElementById("deathSearchInput").oninput=e=>renderDeathTable(e.target.value.trim());
document.getElementById("deathModal").addEventListener("hidden.bs.modal",clearDeathForm);

//========手术记录模块========
function renderOpTable(k=""){
    let list=getOpList().filter(x=>!k||x.opNo.includes(k)||x.patientName.includes(k));
    let t=document.getElementById("operationTableBody");t.innerHTML="";
    list.forEach(item=>{
        let statusBadge="";
        if(item.status==="待手术") statusBadge=`<span class="badge bg-secondary">待手术</span>`;
        else if(item.status==="手术中") statusBadge=`<span class="badge bg-primary">手术中</span>`;
        else if(item.status==="手术完成") statusBadge=`<span class="badge bg-success">手术完成</span>`;
        else if(item.status==="手术取消") statusBadge=`<span class="badge bg-danger">手术取消</span>`;

        t.innerHTML+=`<tr>
            <td>${item.opNo}</td>
            <td>${item.patientName}</td>
            <td>${item.opName}</td>
            <td>${item.startTime||""}</td>
            <td>${statusBadge}</td>
            <td>${item.surgeon}</td>
            <td>
                <button class="btn btn-sm btn-warning op-print" data-opid="${item.id}">打印通知书</button>
                <button class="btn btn-sm btn-info op-edit" data-opid="${item.id}">编辑</button>
                <button class="btn btn-sm btn-danger op-del" data-opid="${item.id}">删除</button>
            </td>
        </tr>`;
    })
}

document.getElementById("saveOpBtn").onclick=function(){
    let opid=document.getElementById("opEditId").value;
    let d={
        id:opid||Date.now()+"",
        opNo:document.getElementById("opNo").value.trim(),
        patientName:document.getElementById("opPatientName").value.trim(),
        hospitalNo:document.getElementById("opHospitalNo").value.trim(),
        gender:document.getElementById("opGender").value,
        age:document.getElementById("opAge").value,
        status:document.getElementById("opStatus").value,
        opName:document.getElementById("opName").value.trim(),
        anaesthesia:document.getElementById("opAnaesthesia").value.trim(),
        startTime:document.getElementById("opStartTime").value,
        endTime:document.getElementById("opEndTime").value,
        bleed:document.getElementById("opBleed").value.trim(),
        surgeon:document.getElementById("opSurgeon").value.trim(),
        assistant:document.getElementById("opAssistant").value.trim(),
        nurse:document.getElementById("opNurse").value.trim(),
        preDiagnosis:document.getElementById("opPreDiagnosis").value.trim(),
        postDiagnosis:document.getElementById("opPostDiagnosis").value.trim(),
        opProcess:document.getElementById("opProcess").value.trim(),
        complication:document.getElementById("opComplication").value.trim(),
        advice:document.getElementById("opAdvice").value.trim()
    };
    if(!d.opNo||!d.patientName)return alert("手术编号、患者姓名不能为空！");
    let arr=getOpList();
    opid?arr[arr.findIndex(x=>x.id===opid)]=d:arr.push(d);
    saveOpList(arr);
    bootstrap.Modal.getInstance(document.getElementById("operationModal")).hide();
    clearOpForm();renderOpTable();
}

function clearOpForm(){
    document.getElementById("opEditId").value="";
    document.getElementById("opNo").value="";
    document.getElementById("opPatientName").value="";
    document.getElementById("opHospitalNo").value="";
    document.getElementById("opGender").value="男";
    document.getElementById("opAge").value="";
    document.getElementById("opStatus").value="待手术";
    document.getElementById("opName").value="";
    document.getElementById("opAnaesthesia").value="";
    document.getElementById("opStartTime").value="";
    document.getElementById("opEndTime").value="";
    document.getElementById("opBleed").value="";
    document.getElementById("opSurgeon").value="";
    document.getElementById("opAssistant").value="";
    document.getElementById("opNurse").value="";
    document.getElementById("opPreDiagnosis").value="";
    document.getElementById("opPostDiagnosis").value="";
    document.getElementById("opProcess").value="";
    document.getElementById("opComplication").value="";
    document.getElementById("opAdvice").value="";
}

document.getElementById("operationTableBody").onclick=e=>{
    let opid=e.target.dataset.opid;if(!opid)return;
    let list=getOpList();
    let item=list.find(x=>x.id===opid);
    if(e.target.classList.contains("op-del")){
        if(confirm("确定删除该手术记录？"))saveOpList(list.filter(x=>x.id!==opid)),renderOpTable();
    }else if(e.target.classList.contains("op-edit")){
        document.getElementById("opEditId").value=item.id;
        document.getElementById("opNo").value=item.opNo;
        document.getElementById("opPatientName").value=item.patientName;
        document.getElementById("opHospitalNo").value=item.hospitalNo;
        document.getElementById("opGender").value=item.gender;
        document.getElementById("opAge").value=item.age;
        document.getElementById("opStatus").value=item.status;
        document.getElementById("opName").value=item.opName;
        document.getElementById("opAnaesthesia").value=item.anaesthesia;
        document.getElementById("opStartTime").value=item.startTime;
        document.getElementById("opEndTime").value=item.endTime;
        document.getElementById("opBleed").value=item.bleed;
        document.getElementById("opSurgeon").value=item.surgeon;
        document.getElementById("opAssistant").value=item.assistant;
        document.getElementById("opNurse").value=item.nurse;
        document.getElementById("opPreDiagnosis").value=item.preDiagnosis;
        document.getElementById("opPostDiagnosis").value=item.postDiagnosis;
        document.getElementById("opProcess").value=item.opProcess;
        document.getElementById("opComplication").value=item.complication;
        document.getElementById("opAdvice").value=item.advice;
        new bootstrap.Modal(document.getElementById("operationModal")).show();
    }else if(e.target.classList.contains("op-print")){
        document.getElementById("opPrintBody").innerHTML=`
<div class="p-4">
    <h4 class="text-center">🏥 手术通知书</h4>
    <hr>
    <p><strong>手术编号：</strong>${item.opNo}</p>
    <p><strong>患者姓名：</strong>${item.patientName} &nbsp;&nbsp;性别：${item.gender} &nbsp;&nbsp;年龄：${item.age}</p>
    <p><strong>住院号：</strong>${item.hospitalNo||"无"}</p>
    <p><strong>手术名称：</strong>${item.opName}</p>
    <p><strong>麻醉方式：</strong>${item.anaesthesia||"无"}</p>
    <p><strong>手术状态：</strong>${item.status}</p>
    <p><strong>拟定手术开始时间：</strong>${item.startTime||""}</p>
    <hr>
    <h5>手术记录</h5>
    <p><strong>术前诊断：</strong>${item.preDiagnosis||"无"}</p>
    <p><strong>术后诊断：</strong>${item.postDiagnosis||"无"}</p>
    <p><strong>主刀医师：</strong>${item.surgeon||""}</p>
    <p><strong>手术助手：</strong>${item.assistant||""}</p>
    <p><strong>器械护士：</strong>${item.nurse||""}</p>
    <p><strong>术中出血量：</strong>${item.bleed||"0"} ml</p>
    <p><strong>手术经过：</strong>${item.opProcess||"无记录"}</p>
    <p><strong>术中并发症：</strong>${item.complication||"无"}</p>
    <p><strong>术后医嘱：</strong>${item.advice||"无"}</p>
    <hr>
    <p class="text-end">医师签字：_______________ &nbsp;&nbsp;日期：_______________</p>
</div>`;
        new bootstrap.Modal(document.getElementById("opPrintModal")).show();
    }
}
document.getElementById("opSearchInput").oninput=e=>renderOpTable(e.target.value.trim());
document.getElementById("operationModal").addEventListener("hidden.bs.modal",clearOpForm);

//页面初始化，全部表格渲染
window.onload=function(){
    renderTable();
    renderHospitalTable();
    renderDocTable();
    renderDeathTable();
    renderOpTable();
}
</script>
</body>
</html>