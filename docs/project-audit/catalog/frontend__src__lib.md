# `frontend/src/lib` 文件清单

本组共 `28` 个文件。

## `frontend/src/lib/apollo.ts`

- 文件类型：`.ts`
- 大小：`20498` 字节
- 文本行数：`531`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.apollo.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`client`
- 直接依赖：`frontend/src/graphql/types.ts`, `frontend/src/lib/log.ts`, `frontend/src/models/api.ts`
- 被这些文件直接引用：`frontend/src/app.tsx`

## `frontend/src/lib/axios.ts`

- 文件类型：`.ts`
- 大小：`9184` 字节
- 文本行数：`250`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.axios.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`ApiErrorResponse, ApiHttpError, ApiResponse, ApiResponseStatus, ApiSuccessResponse, api, isApiSuccess, unwrapApiResponse, getApiErrorMessage, getApiErrorStatusCode`
- 直接依赖：`frontend/src/providers/user-provider.tsx`, `frontend/src/lib/log.ts`, `frontend/src/lib/utils/auth.ts`
- 被这些文件直接引用：`frontend/src/features/authentication/password-change-form.tsx`, `frontend/src/features/flows/files/use-flow-container-files.ts`, `frontend/src/features/flows/files/use-flow-files-attach-resources.ts`, `frontend/src/features/flows/files/use-flow-files-delete.ts`, `frontend/src/features/flows/files/use-flow-files-promote.ts`, `frontend/src/features/flows/files/use-flow-files-pull.ts`, `frontend/src/features/flows/files/use-flow-files-upload.ts`, `frontend/src/features/resources/use-resources-copy.ts`, `frontend/src/features/resources/use-resources-delete.ts`, `frontend/src/features/resources/use-resources-mkdir.ts`, `frontend/src/features/resources/use-resources-move.ts`, `frontend/src/features/resources/use-resources-upload.ts` 等 14 项

## `frontend/src/lib/clipboard.ts`

- 文件类型：`.ts`
- 大小：`5948` 字节
- 文本行数：`183`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.clipboard.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`CopyableMessage, getCleanTerminalText, formatMessageForClipboard, copyMessageToClipboard`
- 直接依赖：`frontend/src/graphql/types.ts`
- 被这些文件直接引用：`frontend/src/features/flows/agents/flow-agent.tsx`, `frontend/src/features/flows/messages/flow-message.tsx`, `frontend/src/features/flows/tools/flow-tool.tsx`, `frontend/src/features/flows/vector-stores/flow-vector-store.tsx`

## `frontend/src/lib/local-storage.ts`

- 文件类型：`.ts`
- 大小：`1365` 字节
- 文本行数：`44`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.local-storage.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`getStorageItem, removeStorageItem, setStorageItem`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/shared/file-manager/file-manager-storage.ts`, `frontend/src/lib/table-state.ts`, `frontend/src/lib/view-options-storage.ts`

## `frontend/src/lib/log.ts`

- 文件类型：`.ts`
- 大小：`963` 字节
- 文本行数：`45`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.log.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`Level, Level, Log`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/shared/monaco-terminal.tsx`, `frontend/src/components/shared/terminal/use-terminal-search.ts`, `frontend/src/components/shared/terminal/use-xterm.ts`, `frontend/src/features/flows/messages/flow-assistant-messages.tsx`, `frontend/src/features/knowledges/knowledge-form.tsx`, `frontend/src/lib/apollo.ts`, `frontend/src/lib/axios.ts`, `frontend/src/lib/report/report-pdf.tsx`, `frontend/src/lib/report/report.ts`, `frontend/src/pages/flows/flow-report.tsx`, `frontend/src/pages/flows/flow.tsx`, `frontend/src/providers/favorites-provider.tsx` 等 16 项

## `frontend/src/lib/report/index.ts`

- 文件类型：`.ts`
- 大小：`171` 字节
- 文本行数：`9`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.report.index.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/report/report.ts`
- 被这些文件直接引用：`frontend/src/features/flows/files/flow-files.tsx`, `frontend/src/pages/flows/flow-report.tsx`, `frontend/src/pages/flows/flow.tsx`, `frontend/src/pages/resources/resources.tsx`

## `frontend/src/lib/report/report-pdf.tsx`

- 文件类型：`.tsx`
- 大小：`18977` 字节
- 文本行数：`641`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.report.report-pdf.tsx`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`generatePDFFromMarkdownNew, generatePDFBlobNew`
- 直接依赖：`frontend/src/lib/log.ts`
- 被这些文件直接引用：`frontend/src/lib/report/report.ts`

## `frontend/src/lib/report/report.ts`

- 文件类型：`.ts`
- 大小：`7106` 字节
- 文本行数：`214`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.report.report.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`generateReport, generateFileName, downloadTextFile, copyToClipboard, generatePDFFromMarkdown, generatePDFBlob`
- 直接依赖：`frontend/src/graphql/types.ts`, `frontend/src/lib/log.ts`, `frontend/src/lib/report/report-pdf.tsx`
- 被这些文件直接引用：`frontend/src/lib/report/index.ts`

## `frontend/src/lib/route-titles/apollo-title.test.tsx`

- 文件类型：`.tsx`
- 大小：`2021` 字节
- 文本行数：`48`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.route-titles.apollo-title.test.tsx`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/route-titles/apollo-title.tsx`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/route-titles/apollo-title.tsx`

- 文件类型：`.tsx`
- 大小：`3493` 字节
- 文本行数：`77`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.route-titles.apollo-title.tsx`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`ApolloTitleComponent, isApolloTitle, apolloTitle`
- 直接依赖：`frontend/src/lib/route-titles/render-title.tsx`
- 被这些文件直接引用：`frontend/src/components/shared/document-title.test.tsx`, `frontend/src/components/shared/document-title.tsx`, `frontend/src/lib/route-titles/apollo-title.test.tsx`, `frontend/src/lib/route-titles/index.ts`

## `frontend/src/lib/route-titles/format-prompt-id.ts`

- 文件类型：`.ts`
- 大小：`696` 字节
- 文本行数：`18`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.route-titles.format-prompt-id.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`formatPromptId`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/lib/route-titles/index.ts`, `frontend/src/pages/settings/settings-prompt.tsx`

## `frontend/src/lib/route-titles/index.ts`

- 文件类型：`.ts`
- 大小：`3751` 字节
- 文本行数：`99`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.route-titles.index.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`RouteTitleHandle, TitleResolver, routeTitles`
- 直接依赖：`frontend/src/graphql/types.ts`, `frontend/src/lib/route-titles/apollo-title.tsx`, `frontend/src/lib/route-titles/format-prompt-id.ts`, `frontend/src/lib/route-titles/render-title.tsx`
- 被这些文件直接引用：`frontend/src/app.tsx`

## `frontend/src/lib/route-titles/render-title.tsx`

- 文件类型：`.tsx`
- 大小：`448` 字节
- 文本行数：`9`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.route-titles.render-title.tsx`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`APP_NAME, RouteParams, renderTitle`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/shared/document-title.tsx`, `frontend/src/lib/route-titles/apollo-title.tsx`, `frontend/src/lib/route-titles/index.ts`

## `frontend/src/lib/storage-keys.test.ts`

- 文件类型：`.ts`
- 大小：`1867` 字节
- 文本行数：`55`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.storage-keys.test.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/storage-keys.ts`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/storage-keys.ts`

- 文件类型：`.ts`
- 大小：`3507` 字节
- 文本行数：`82`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.storage-keys.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`STORAGE_KEY_SEPARATOR, LocalStorageKeyType, getPeriodStorageKey, getStorageKey, getTableStorageKey, getTopLevelPath, getViewOptionsStorageKey`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/hooks/use-page-storage-keys.ts`, `frontend/src/lib/storage-keys.test.ts`, `frontend/src/lib/table-state.ts`

## `frontend/src/lib/table-state.test.ts`

- 文件类型：`.ts`
- 大小：`8054` 字节
- 文本行数：`189`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.table-state.test.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/table-state.ts`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/table-state.ts`

- 文件类型：`.ts`
- 大小：`5763` 字节
- 文本行数：`145`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.table-state.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`TableState, loadTableState, updateTableState, migrateLegacyTableState`
- 直接依赖：`frontend/src/lib/local-storage.ts`, `frontend/src/lib/storage-keys.ts`
- 被这些文件直接引用：`frontend/src/components/ui/data-table.tsx`, `frontend/src/lib/table-state.test.ts`

## `frontend/src/lib/upload-validation.test.ts`

- 文件类型：`.ts`
- 大小：`3077` 字节
- 文本行数：`78`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.upload-validation.test.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/upload-validation.ts`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/upload-validation.ts`

- 文件类型：`.ts`
- 大小：`2498` 字节
- 文本行数：`67`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.upload-validation.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`UploadValidationLimits, validateUploadBatch`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/features/flows/files/use-flow-files-upload.ts`, `frontend/src/features/resources/use-resources-upload.ts`, `frontend/src/lib/upload-validation.test.ts`

## `frontend/src/lib/url-params.test.ts`

- 文件类型：`.ts`
- 大小：`2010` 字节
- 文本行数：`45`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.url-params.test.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/url-params.ts`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/url-params.ts`

- 文件类型：`.ts`
- 大小：`2409` 字节
- 文本行数：`61`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.url-params.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`URL_PARAMS, mergeHrefWithSearchParams`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/shared/detail-navigation/use-detail-navigation.ts`, `frontend/src/hooks/use-table-query-filter.ts`, `frontend/src/hooks/use-table-state.ts`, `frontend/src/lib/url-params.test.ts`, `frontend/src/pages/flows/flows.tsx`, `frontend/src/pages/knowledges/knowledges.tsx`, `frontend/src/pages/templates/templates.tsx`, `frontend/src/providers/knowledges-provider.tsx`

## `frontend/src/lib/utils.test.ts`

- 文件类型：`.ts`
- 大小：`173` 字节
- 文本行数：`8`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.utils.test.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/utils.ts`

- 文件类型：`.ts`
- 大小：`203` 字节
- 文本行数：`9`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.utils.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`cn`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/icons/anthropic.tsx`, `frontend/src/components/icons/bedrock.tsx`, `frontend/src/components/icons/custom.tsx`, `frontend/src/components/icons/deepseek.tsx`, `frontend/src/components/icons/flow-status-icon.tsx`, `frontend/src/components/icons/gemini.tsx`, `frontend/src/components/icons/github.tsx`, `frontend/src/components/icons/glm.tsx`, `frontend/src/components/icons/google.tsx`, `frontend/src/components/icons/kimi.tsx`, `frontend/src/components/icons/logo.tsx`, `frontend/src/components/icons/ollama.tsx` 等 90 项

## `frontend/src/lib/utils/auth.ts`

- 文件类型：`.ts`
- 大小：`1022` 字节
- 文本行数：`32`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.utils.auth.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`getReturnUrlParam, getSafeReturnUrl`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/routes/protected-route.tsx`, `frontend/src/components/routes/public-route.tsx`, `frontend/src/lib/axios.ts`, `frontend/src/pages/login.tsx`, `frontend/src/providers/user-provider.tsx`

## `frontend/src/lib/utils/format.ts`

- 文件类型：`.ts`
- 大小：`1934` 字节
- 文本行数：`77`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.utils.format.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`formatName, formatDate, formatNumber, formatTokenCount, formatCost, formatDuration`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/dashboard/chart-tooltip.tsx`, `frontend/src/features/flows/agents/flow-agent-icon.tsx`, `frontend/src/features/flows/agents/flow-agent.tsx`, `frontend/src/features/flows/dashboard/flow-dashboard-overview.tsx`, `frontend/src/features/flows/messages/flow-assistant-messages.tsx`, `frontend/src/features/flows/messages/flow-message-type-icon.tsx`, `frontend/src/features/flows/messages/flow-message.tsx`, `frontend/src/features/flows/screenshots/flow-screenshot.tsx`, `frontend/src/features/flows/tasks/flow-task-status-icon.tsx`, `frontend/src/features/flows/tools/flow-tool.tsx`, `frontend/src/features/flows/vector-stores/flow-vector-store-action-icon.tsx`, `frontend/src/features/flows/vector-stores/flow-vector-store.tsx` 等 18 项

## `frontend/src/lib/utils/platform.ts`

- 文件类型：`.ts`
- 大小：`408` 字节
- 文本行数：`13`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.utils.platform.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`isMac`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`frontend/src/components/shared/terminal/use-xterm.ts`, `frontend/src/components/ui/input-search.tsx`

## `frontend/src/lib/view-options-storage.test.ts`

- 文件类型：`.ts`
- 大小：`5068` 字节
- 文本行数：`123`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.view-options-storage.test.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`frontend/src/lib/view-options-storage.ts`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `frontend/src/lib/view-options-storage.ts`

- 文件类型：`.ts`
- 大小：`1762` 字节
- 文本行数：`50`
- 所属分组：`frontend/src/lib`
- 所属包/模块：`frontend.src.lib.view-options-storage.ts`
- 推断作用：前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。
- 生成文件：`否`
- 关键导出/符号：`ViewOptionsRecord, loadViewOptions, saveViewOptions, migrateLegacyViewOptions`
- 直接依赖：`frontend/src/lib/local-storage.ts`
- 被这些文件直接引用：`frontend/src/lib/view-options-storage.test.ts`, `frontend/src/pages/resources/resources.tsx`
