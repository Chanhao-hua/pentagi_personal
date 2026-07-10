# `backend/pkg/server` 文件清单

本组共 `92` 个文件。

## `backend/pkg/server/auth/api_token_cache.go`

- 文件类型：`.go`
- 大小：`3189` 字节
- 文本行数：`122`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TokenCache, NewTokenCache, SetTTL, GetStatus, Invalidate, InvalidateUser, InvalidateAll`
- 直接依赖：`backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/api_token_cache_test.go`

- 文件类型：`.go`
- 大小：`8846` 字节
- 文本行数：`323`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestTokenCache_GetStatus, TestTokenCache_Invalidate, TestTokenCache_InvalidateUser, TestTokenCache_Expiration, TestTokenCache_PrivilegesByRole, TestTokenCache_NegativeCaching, TestTokenCache_NegativeCachingExpiration`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/auth/api_token_id.go`

- 文件类型：`.go`
- 大小：`608` 字节
- 文本行数：`29`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`GenerateTokenID`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/api_token_id_test.go`

- 文件类型：`.go`
- 大小：`1447` 字节
- 文本行数：`50`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestGenerateTokenID, TestGenerateTokenIDFormat`
- 直接依赖：`backend/pkg/server/auth`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/auth/api_token_jwt.go`

- 文件类型：`.go`
- 大小：`1782` 字节
- 文本行数：`63`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`MakeAPIToken, MakeAPITokenClaims, ValidateAPIToken`
- 直接依赖：`backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/api_token_test.go`

- 文件类型：`.go`
- 大小：`13968` 字节
- 文本行数：`480`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestValidateAPIToken, TestAPITokenAuthentication_CacheExpiration, TestAPITokenAuthentication_DefaultSalt, TestAPITokenAuthentication_SoftDelete, TestAPITokenAuthentication_AlgNoneAttack, TestAPITokenAuthentication_LegacyProtoToken`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/auth/auth_middleware.go`

- 文件类型：`.go`
- 大小：`6458` 字节
- 文本行数：`238`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`AuthMiddleware, NewAuthMiddleware, AuthUserRequired, AuthTokenRequired, TryAuth, PrivilegeAutomation`
- 直接依赖：`backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/auth_middleware_test.go`

- 文件类型：`.go`
- 大小：`9507` 字节
- 文本行数：`338`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestAuthTokenProtoRequiredAuthWithCookie, TestAuthTokenProtoRequiredAuthWithToken, TestAuthRequiredAuthWithCookie, Authorize, GetToken, SetSessionCheckFunc, Unauthorize, TestCall, TestCallWithData, Called, CallAndGetStatus`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/auth/integration_test.go`

- 文件类型：`.go`
- 大小：`26448` 字节
- 文本行数：`891`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestEndToEndAPITokenFlow, TestAPIToken_RoleIsolation, TestAPIToken_SignatureVerification, TestAPIToken_CacheInvalidation, TestAPIToken_ConcurrentAccess, TestAPIToken_JSONStructure, TestAPIToken_Expiration, TestDualAuthentication, TestSecurityAudit_ClaimsInJWT, TestSecurityAudit_TokenIDUniqueness, TestSecurityAudit_SaltIsolation, TestAPIToken_ContextSetup`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。；长文件（891 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/auth/permissions.go`

- 文件类型：`.go`
- 大小：`876` 字节
- 文本行数：`47`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`PrivilegesRequired, LookupPerm`
- 直接依赖：`backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/permissions_test.go`

- 文件类型：`.go`
- 大小：`1013` 字节
- 文本行数：`37`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestPrivilegesRequired`
- 直接依赖：`backend/pkg/server/auth`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/auth/session.go`

- 文件类型：`.go`
- 大小：`2284` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`MakeCookieStoreKey, MakeJWTSigningKey`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/session_test.go`

- 文件类型：`.go`
- 大小：`2028` 字节
- 文本行数：`62`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestMakeJWTSigningKey, TestMakeCookieStoreKey, TestMakeJWTSigningKeyDifferentFromCookieKey`
- 直接依赖：`backend/pkg/server/auth`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/auth/users_cache.go`

- 文件类型：`.go`
- 大小：`2201` 字节
- 文本行数：`93`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`UserCache, NewUserCache, SetTTL, GetUserHash, Invalidate, InvalidateAll`
- 直接依赖：`backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项

## `backend/pkg/server/auth/users_cache_test.go`

- 文件类型：`.go`
- 大小：`11240` 字节
- 文本行数：`444`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`auth_test`
- 推断作用：认证与鉴权支持文件，负责 Token、会话或用户身份校验。
- 生成文件：`否`
- 关键导出/符号：`TestUserCache_GetUserHash, TestUserCache_Invalidate, TestUserCache_Expiration, TestUserCache_UserStatuses, TestUserCache_DeletedUser, TestUserCache_ConcurrentAccess, TestUserCache_InvalidateAll, TestUserCache_NegativeCaching, TestUserCache_NegativeCachingExpiration`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_id_test.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/permissions_test.go`, `backend/pkg/server/auth/session_test.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/api_tokens.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/context/context.go`

- 文件类型：`.go`
- 大小：`1508` 字节
- 文本行数：`62`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`context`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`GetInt64, GetUint64, GetString, GetStringArray, GetStringFromSession`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/server/context/context_test.go`

- 文件类型：`.go`
- 大小：`11207` 字节
- 文本行数：`511`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`context`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestGetInt64, TestGetUint64, TestGetString, TestGetStringArray, TestGetStringFromSession, TestMultipleValuesInContext, TestContextOverwrite, TestContextTypeChange`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/docs/docs.go`

- 文件类型：`.go`
- 大小：`399825` 字节
- 文本行数：`10501`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`docs`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`是`
- 关键导出/符号：`SwaggerInfo`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（10501 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/docs/swagger.json`

- 文件类型：`.json`
- 大小：`399137` 字节
- 文本行数：`10476`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`未识别`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`是`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（10476 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/docs/swagger.yaml`

- 文件类型：`.yaml`
- 大小：`195763` 字节
- 文本行数：`7078`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`未识别`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`是`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（7078 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/logger/logger.go`

- 文件类型：`.go`
- 大小：`2597` 字节
- 文本行数：`100`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`logger`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`FromContext, TraceEnabled, WithGinLogger, WithGqlLogger`
- 直接依赖：`backend/pkg/observability`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/response/http.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/agentlogs.go`, `backend/pkg/server/services/analytics.go`, `backend/pkg/server/services/anonymizer.go`, `backend/pkg/server/services/api_tokens.go`, `backend/pkg/server/services/assistantlogs.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/auth.go`, `backend/pkg/server/services/containers.go`, `backend/pkg/server/services/flow_files.go`, `backend/pkg/server/services/flows.go` 等 28 项

## `backend/pkg/server/middleware.go`

- 文件类型：`.go`
- 大小：`1356` 字节
- 文本行数：`52`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`router`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/server/models`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`

## `backend/pkg/server/models/agentlogs.go`

- 文件类型：`.go`
- 大小：`1682` 字节
- 文本行数：`39`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`Agentlog, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/analytics.go`

- 文件类型：`.go`
- 大小：`16897` 字节
- 文本行数：`547`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`UsageStatsPeriod, String, Valid, Validate, UsageStats, Valid, Validate, ToolcallsStats, Valid, Validate, FlowsStats, Valid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/api_tokens.go`

- 文件类型：`.go`
- 大小：`4695` 字节
- 文本行数：`134`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TokenStatus, String, Valid, Validate, APIToken, TableName, Valid, Validate, APITokenWithSecret, Valid, CreateAPITokenRequest, Valid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/api_tokens_test.go`

- 文件类型：`.go`
- 大小：`5977` 字节
- 文本行数：`256`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestTokenStatusValid, TestTokenStatusString, TestAPITokenValid, TestAPITokenTableName, TestCreateAPITokenRequestValid, TestUpdateAPITokenRequestValid, TestAPITokenWithSecretValid, TestAPITokenClaimsValid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/assistantlogs.go`

- 文件类型：`.go`
- 大小：`1858` 字节
- 文本行数：`39`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`Assistantlog, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/assistants.go`

- 文件类型：`.go`
- 大小：`6072` 字节
- 文本行数：`134`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`AssistantStatus, String, Valid, Validate, Assistant, TableName, Valid, Validate, CreateAssistant, Valid, PatchAssistant, Valid`
- 直接依赖：`backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/assistants_test.go`

- 文件类型：`.go`
- 大小：`5186` 字节
- 文本行数：`212`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestAssistantStatusValid, TestAssistantStatusString, TestAssistantValid, TestAssistantTableName, TestCreateAssistantValid, TestPatchAssistantValid, TestAssistantFlowValid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/containers.go`

- 文件类型：`.go`
- 大小：`3451` 字节
- 文本行数：`104`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`ContainerStatus, String, Valid, Validate, ContainerType, String, Valid, Validate, Container, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/flow_files.go`

- 文件类型：`.go`
- 大小：`3282` 字节
- 文本行数：`80`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`FlowFile, FlowFiles, ContainerFile, ContainerFiles, PullFlowFilesRequest, AddResourcesRequest, AddResourceFromFlowRequest`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/flows.go`

- 文件类型：`.go`
- 大小：`6802` 字节
- 文本行数：`169`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`FlowStatus, String, Valid, Validate, Flow, TableName, Valid, Validate, CreateFlow, Valid, PatchFlow, Valid`
- 直接依赖：`backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/flows_test.go`

- 文件类型：`.go`
- 大小：`16168` 字节
- 文本行数：`712`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestFlowStatusValid, TestFlowStatusString, TestFlowTableName, TestCreateFlowValid, TestPatchFlowValid, TestTaskStatusValid, TestTaskTableName, TestSubtaskStatusValid, TestSubtaskTableName, TestContainerStatusValid, TestContainerTypeValid, TestContainerTableName`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/init.go`

- 文件类型：`.go`
- 大小：`6639` 字节
- 文本行数：`265`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`GetValidator, IsStrongPassword, IValid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/init_test.go`

- 文件类型：`.go`
- 大小：`5550` 字节
- 文本行数：`253`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestGetValidator, TestStrongPasswordValidator, TestEmailValidator, TestOAuthMinScopeValidator, TestSolidValidator, TestSemverValidator, TestSemverExValidator, TestScanFromJSON`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/knowledge.go`

- 文件类型：`.go`
- 大小：`16173` 字节
- 文本行数：`477`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`KnowledgeDocType, Valid, KnowledgeGuideType, Valid, KnowledgeAnswerType, Valid, KnowledgeDocEntry, KnowledgeDocList, KnowledgeEmbeddingRow, KnowledgeDocWithScore, KnowledgeSearchResult, KnowledgeListQuery`
- 直接依赖：`backend/pkg/graph/model`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/msgchains.go`

- 文件类型：`.go`
- 大小：`2008` 字节
- 文本行数：`68`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`MsgchainType, Scan, String, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/msglogs.go`

- 文件类型：`.go`
- 大小：`3906` 字节
- 文本行数：`112`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`MsglogType, String, Valid, Validate, MsglogResultFormat, String, Valid, Validate, Msglog, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/prompts.go`

- 文件类型：`.go`
- 大小：`3708` 字节
- 文本行数：`93`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`PromptType, String, Valid, Validate, Prompt, TableName, Valid, Validate, PatchPrompt, Valid`
- 直接依赖：`backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/prompts_test.go`

- 文件类型：`.go`
- 大小：`2637` 字节
- 文本行数：`112`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestPromptTypeValid, TestPromptTypeString, TestPromptValid, TestPromptTableName, TestPatchPromptValid`
- 直接依赖：`backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/providers.go`

- 文件类型：`.go`
- 大小：`5009` 字节
- 文本行数：`134`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`ProviderType, String, Valid, Validate, Provider, TableName, Valid, Validate, CreateProvider, Valid, PatchProvider, Valid`
- 直接依赖：`backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/providers_test.go`

- 文件类型：`.go`
- 大小：`4056` 字节
- 文本行数：`184`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestProviderTypeValid, TestProviderTypeString, TestProviderValid, TestProviderTableName, TestCreateProviderValid, TestPatchProviderValid, TestProviderInfoValid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/resources.go`

- 文件类型：`.go`
- 大小：`4382` 字节
- 文本行数：`92`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`UserResource, ResourceEntry, ResourceList, MkdirResourceRequest, MoveResourceRequest, CopyResourceRequest`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/roles.go`

- 文件类型：`.go`
- 大小：`2327` 字节
- 文本行数：`75`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`Role, TableName, Valid, Validate, Privilege, TableName, Valid, RolePrivileges, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/screenshots.go`

- 文件类型：`.go`
- 大小：`1438` 字节
- 文本行数：`37`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`Screenshot, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/searchlogs.go`

- 文件类型：`.go`
- 大小：`2988` 字节
- 文本行数：`80`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`SearchEngineType, String, Valid, Validate, Searchlog, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/settings.go`

- 文件类型：`.go`
- 大小：`638` 字节
- 文本行数：`18`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`Settings, Valid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/subtasks.go`

- 文件类型：`.go`
- 大小：`2622` 字节
- 文本行数：`75`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`SubtaskStatus, String, Valid, Validate, Subtask, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/tasks.go`

- 文件类型：`.go`
- 大小：`3248` 字节
- 文本行数：`103`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TaskStatus, String, Valid, Validate, Task, TableName, Valid, Validate, TaskSubtasks, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/termlogs.go`

- 文件类型：`.go`
- 大小：`2268` 字节
- 文本行数：`68`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TermlogType, String, Valid, Validate, Termlog, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/toolcalls.go`

- 文件类型：`.go`
- 大小：`3010` 字节
- 文本行数：`76`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`ToolcallStatus, String, Valid, Validate, Toolcall, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/users.go`

- 文件类型：`.go`
- 大小：`9573` 字节
- 文本行数：`305`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`RoleUser, UserStatus, String, Valid, Validate, UserType, String, Valid, Validate, User, TableName, Valid`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/models/users_test.go`

- 文件类型：`.go`
- 大小：`12683` 字节
- 文本行数：`579`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestUserStatusValid, TestUserStatusString, TestUserTypeValid, TestUserTypeString, TestLoginValid, TestPasswordValid, TestUserValid, TestUserTableName, TestUserPasswordValid, TestUserPasswordTableName, TestLoginTableName, TestPasswordTableName`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/models/vecstorelogs.go`

- 文件类型：`.go`
- 大小：`2641` 字节
- 文本行数：`70`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`models`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`VecstoreActionType, String, Valid, Validate, Vecstorelog, TableName, Valid, Validate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/pkg/server/auth/api_token_cache.go`, `backend/pkg/server/auth/api_token_cache_test.go`, `backend/pkg/server/auth/api_token_jwt.go`, `backend/pkg/server/auth/api_token_test.go`, `backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/auth_middleware_test.go`, `backend/pkg/server/auth/integration_test.go`, `backend/pkg/server/auth/users_cache.go`, `backend/pkg/server/auth/users_cache_test.go`, `backend/pkg/server/middleware.go` 等 40 项

## `backend/pkg/server/oauth/client.go`

- 文件类型：`.go`
- 大小：`2109` 字节
- 文本行数：`65`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`oauth`
- 推断作用：第三方 OAuth 登录适配文件，封装 Google/GitHub 等登录流程。
- 生成文件：`否`
- 关键导出/符号：`OAuthEmailResolver, OAuthClient, NewOAuthClient, ProviderName, ResolveEmail, TokenSource, Exchange, RefreshToken, AuthCodeURL`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`, `backend/pkg/server/services/auth.go`

## `backend/pkg/server/oauth/github.go`

- 文件类型：`.go`
- 大小：`1563` 字节
- 文本行数：`71`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`oauth`
- 推断作用：第三方 OAuth 登录适配文件，封装 Google/GitHub 等登录流程。
- 生成文件：`否`
- 关键导出/符号：`NewGithubOAuthClient`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`, `backend/pkg/server/services/auth.go`

## `backend/pkg/server/oauth/google.go`

- 文件类型：`.go`
- 大小：`2160` 字节
- 文本行数：`77`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`oauth`
- 推断作用：第三方 OAuth 登录适配文件，封装 Google/GitHub 等登录流程。
- 生成文件：`否`
- 关键导出/符号：`NewGoogleOAuthClient`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`, `backend/pkg/server/services/auth.go`

## `backend/pkg/server/rdb/table.go`

- 文件类型：`.go`
- 大小：`11723` 字节
- 文本行数：`371`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`rdb`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TableFilter, TableSort, TableQuery, Init, DoConditionFormat, SetFilters, SetFind, SetOrders, Find, Mappers, Table, Ordering`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/services/agentlogs.go`, `backend/pkg/server/services/assistantlogs.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/auth.go`, `backend/pkg/server/services/containers.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/knowledge.go`, `backend/pkg/server/services/msglogs.go`, `backend/pkg/server/services/prompts.go`, `backend/pkg/server/services/roles.go`, `backend/pkg/server/services/screenshots.go` 等 19 项

## `backend/pkg/server/response/errors.go`

- 文件类型：`.go`
- 大小：`10602` 字节
- 文本行数：`172`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`response`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`ErrInternal, ErrInternalDBNotFound, ErrInternalServiceNotFound, ErrInternalDBEncryptorNotFound, ErrNotPermitted, ErrAuthRequired, ErrLocalUserRequired, ErrPrivilegesRequired, ErrAdminRequired, ErrSuperRequired, ErrAuthInvalidLoginRequest, ErrAuthInvalidAuthorizeQuery`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/permissions.go`, `backend/pkg/server/middleware.go`, `backend/pkg/server/services/agentlogs.go`, `backend/pkg/server/services/analytics.go`, `backend/pkg/server/services/anonymizer.go`, `backend/pkg/server/services/api_tokens.go`, `backend/pkg/server/services/assistantlogs.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/auth.go`, `backend/pkg/server/services/containers.go`, `backend/pkg/server/services/flow_files.go` 等 28 项

## `backend/pkg/server/response/http.go`

- 文件类型：`.go`
- 大小：`1764` 字节
- 文本行数：`76`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`response`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`HttpError, Code, HttpCode, Msg, NewHttpError, Error, Error, Success`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/permissions.go`, `backend/pkg/server/middleware.go`, `backend/pkg/server/services/agentlogs.go`, `backend/pkg/server/services/analytics.go`, `backend/pkg/server/services/anonymizer.go`, `backend/pkg/server/services/api_tokens.go`, `backend/pkg/server/services/assistantlogs.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/auth.go`, `backend/pkg/server/services/containers.go`, `backend/pkg/server/services/flow_files.go` 等 28 项

## `backend/pkg/server/response/http_test.go`

- 文件类型：`.go`
- 大小：`15332` 字节
- 文本行数：`435`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`response`
- 推断作用：后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。
- 生成文件：`否`
- 关键导出/符号：`TestNewHttpError, TestHttpError_Error, TestHttpError_ImplementsError, TestPredefinedErrors, TestSuccessResponse, TestSuccessResponse_Created, TestErrorResponse, TestErrorResponse_DevMode, TestErrorResponse_ProductionMode, TestErrorResponse_NilOriginalError, TestHttpError_MultipleInstancesIndependent, TestSuccessResponse_EmptyData`
- 直接依赖：`backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/auth/auth_middleware.go`, `backend/pkg/server/auth/permissions.go`, `backend/pkg/server/middleware.go`, `backend/pkg/server/services/agentlogs.go`, `backend/pkg/server/services/analytics.go`, `backend/pkg/server/services/anonymizer.go`, `backend/pkg/server/services/api_tokens.go`, `backend/pkg/server/services/assistantlogs.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/auth.go`, `backend/pkg/server/services/containers.go`, `backend/pkg/server/services/flow_files.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/router.go`

- 文件类型：`.go`
- 大小：`21833` 字节
- 文本行数：`697`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`router`
- 推断作用：Gin 路由总装配文件，绑定 REST、GraphQL、认证、中间件和前端静态资源回退逻辑。
- 生成文件：`否`
- 关键导出/符号：`NewRouter`
- 直接依赖：`backend/pkg/config`, `backend/pkg/controller`, `backend/pkg/database`, `backend/pkg/database/knowledge`, `backend/pkg/docker`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`, `backend/pkg/server/auth`, `backend/pkg/server/logger`, `backend/pkg/server/oauth`, `backend/pkg/server/services`, `backend/pkg/server/docs`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`

## `backend/pkg/server/services/agentlogs.go`

- 文件类型：`.go`
- 大小：`7076` 字节
- 文本行数：`221`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`AgentlogService, NewAgentlogService, GetAgentlogs, GetFlowAgentlogs`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/analytics.go`

- 文件类型：`.go`
- 大小：`36853` 字节
- 文本行数：`1038`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`AnalyticsService, NewAnalyticsService, GetSystemUsage, GetPeriodUsage, GetFlowUsage`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/response`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：长文件（1038 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/anonymizer.go`

- 文件类型：`.go`
- 大小：`2132` 字节
- 文本行数：`68`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`AnonymizerService, NewAnonymizerService, AnonymizeText`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/api_tokens.go`

- 文件类型：`.go`
- 大小：`14422` 字节
- 文本行数：`437`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`TokenService, NewTokenService, CreateToken, ListTokens, GetToken, UpdateToken, DeleteToken`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`, `backend/pkg/server/auth`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/api_tokens_test.go`

- 文件类型：`.go`
- 大小：`34614` 字节
- 文本行数：`1129`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`TestTokenService_CreateToken, TestTokenService_CreateTokenRejectsAPITokenPrincipal, TestTokenService_CreateToken_NameUniqueness, TestTokenService_ListTokens, TestTokenService_GetToken, TestTokenService_UpdateToken, TestTokenService_UpdateToken_NameUniqueness, TestTokenService_DeleteToken, TestTokenService_DeleteToken_InvalidatesCache, TestTokenService_UpdateToken_InvalidatesCache, TestTokenService_FullLifecycle, TestTokenService_AdminPermissions`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1129 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/assistantlogs.go`

- 文件类型：`.go`
- 大小：`7383` 字节
- 文本行数：`220`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`AssistantlogService, NewAssistantlogService, GetAssistantlogs, GetFlowAssistantlogs`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/assistants.go`

- 文件类型：`.go`
- 大小：`24033` 字节
- 文本行数：`685`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`AssistantService, NewAssistantService, GetFlowAssistants, GetFlowAssistant, CreateFlowAssistant, PatchAssistant, DeleteAssistant`
- 直接依赖：`backend/pkg/controller`, `backend/pkg/database`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`, `backend/pkg/providers/provider`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/auth.go`

- 文件类型：`.go`
- 大小：`28376` 字节
- 文本行数：`891`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`AuthServiceConfig, AuthService, NewAuthService, AuthLogin, AuthAuthorize, AuthLoginGetCallback, AuthLoginPostCallback, AuthLogoutCallback, AuthLogout, Info`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/oauth`, `backend/pkg/server/rdb`, `backend/pkg/server/response`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：长文件（891 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/containers.go`

- 文件类型：`.go`
- 大小：`9727` 字节
- 文本行数：`288`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`ContainerService, NewContainerService, GetContainers, GetFlowContainers, GetFlowContainer`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/flow_files.go`

- 文件类型：`.go`
- 大小：`76237` 字节
- 文本行数：`2051`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`FlowFileService, NewFlowFileService, GetFlowFiles, UploadFlowFiles, DeleteFlowFile, DownloadFlowFile, PullFlowFiles, GetFlowContainerFiles, AddResourcesToFlow, AddResourceFromFlow`
- 直接依赖：`backend/pkg/docker`, `backend/pkg/flowfiles`, `backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`, `backend/pkg/resources`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/response`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：长文件（2051 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/flow_files_test.go`

- 文件类型：`.go`
- 大小：`155254` 字节
- 文本行数：`4151`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`TestSanitizeFlowFileName, TestSanitizeContainerCachePath, TestFlowFileService_Dirs, TestMaxUploadFileSize, TestResolveCachedPath, TestListDirEntries_Basic, TestListDirEntries_MissingDir, TestListDirEntriesRecursive_PreservesNestedPaths, TestFlowFileService_ListFlowFiles_BothSources, TestFlowFileService_ListFlowFiles_EmptyDirs, TestConvertModelFlowFile_PreservesID, TestConvertContainerFiles`
- 直接依赖：`backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/flowfiles`, `backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers/pconfig`, `backend/pkg/resources`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（4151 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/flows.go`

- 文件类型：`.go`
- 大小：`22463` 字节
- 文本行数：`676`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`FlowService, NewFlowService, GetFlows, GetFlow, GetFlowGraph, CreateFlow, PatchFlow, DeleteFlow`
- 直接依赖：`backend/pkg/controller`, `backend/pkg/database`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`, `backend/pkg/providers/provider`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/graphql.go`

- 文件类型：`.go`
- 大小：`6009` 字节
- 文本行数：`228`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`GraphqlService, NewGraphqlService, ServeGraphql, ServeGraphqlPlayground`
- 直接依赖：`backend/pkg/config`, `backend/pkg/controller`, `backend/pkg/database`, `backend/pkg/database/knowledge`, `backend/pkg/graph`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`, `backend/pkg/server/auth`, `backend/pkg/server/logger`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/knowledge.go`

- 文件类型：`.go`
- 大小：`19576` 字节
- 文本行数：`520`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`KnowledgeService, NewKnowledgeService, ListDocuments, GetDocument, SearchDocuments, CreateDocument, UpdateDocument, DeleteDocument`
- 直接依赖：`backend/pkg/database/knowledge`, `backend/pkg/graph/model`, `backend/pkg/server/auth`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/msglogs.go`

- 文件类型：`.go`
- 大小：`7097` 字节
- 文本行数：`222`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`MsglogService, NewMsglogService, GetMsglogs, GetFlowMsglogs`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/prompts.go`

- 文件类型：`.go`
- 大小：`13372` 字节
- 文本行数：`392`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`PromptService, NewPromptService, GetPrompts, GetPrompt, PatchPrompt, ResetPrompt, DeletePrompt`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/providers.go`

- 文件类型：`.go`
- 大小：`3398` 字节
- 文本行数：`124`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`ProviderService, NewProviderService, GetProviders`
- 直接依赖：`backend/pkg/providers`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/resources.go`

- 文件类型：`.go`
- 大小：`75865` 字节
- 文本行数：`2267`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`ResourceService, NewResourceService, ListResources, UploadResources, MkdirResource, MoveResource, CopyResource, DeleteResource, DownloadResource`
- 直接依赖：`backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`, `backend/pkg/resources`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：长文件（2267 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/resources_test.go`

- 文件类型：`.go`
- 大小：`113010` 字节
- 文本行数：`3034`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`NewFlowSubscriber, NewFlowPublisher, NewResourceSubscriber, NewProviderSubscriber, NewProviderPublisher, NewAPITokenSubscriber, NewAPITokenPublisher, NewSettingsSubscriber, NewSettingsPublisher, NewFlowTemplateSubscriber, NewFlowTemplatePublisher, NewResourcePublisher`
- 直接依赖：`backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`, `backend/pkg/resources`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（3034 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/server/services/roles.go`

- 文件类型：`.go`
- 大小：`4811` 字节
- 文本行数：`165`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`RoleService, NewRoleService, GetRoles, GetRole`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/screenshots.go`

- 文件类型：`.go`
- 大小：`12150` 字节
- 文本行数：`355`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`ScreenshotService, NewScreenshotService, GetScreenshots, GetFlowScreenshots, GetFlowScreenshot, GetFlowScreenshotFile`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/searchlogs.go`

- 文件类型：`.go`
- 大小：`7185` 字节
- 文本行数：`222`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`SearchlogService, NewSearchlogService, GetSearchlogs, GetFlowSearchlogs`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/settings.go`

- 文件类型：`.go`
- 大小：`1397` 字节
- 文本行数：`51`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`SettingsService, NewSettingsService, GetSettings`
- 直接依赖：`backend/pkg/config`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/response`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/subtasks.go`

- 文件类型：`.go`
- 大小：`11093` 字节
- 文本行数：`322`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`SubtaskService, NewSubtaskService, GetFlowSubtasks, GetFlowTaskSubtasks, GetFlowTaskSubtask`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/tasks.go`

- 文件类型：`.go`
- 大小：`9891` 字节
- 文本行数：`308`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`TaskService, NewTaskService, GetFlowTasks, GetFlowTask, GetFlowTaskGraph`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/termlogs.go`

- 文件类型：`.go`
- 大小：`6984` 字节
- 文本行数：`220`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`TermlogService, NewTermlogService, GetTermlogs, GetFlowTermlogs`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/toolcalls.go`

- 文件类型：`.go`
- 大小：`9814` 字节
- 文本行数：`291`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`ToolcallService, NewToolcallService, GetToolcalls, GetFlowToolcalls, GetFlowToolcall`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/users.go`

- 文件类型：`.go`
- 大小：`22769` 字节
- 文本行数：`685`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`UserService, NewUserService, GetCurrentUser, ChangePasswordCurrentUser, GetUsers, GetUser, CreateUser, PatchUser, DeleteUser, GetUserPrivileges, CheckPrivilege`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`

## `backend/pkg/server/services/users_test.go`

- 文件类型：`.go`
- 大小：`9842` 字节
- 文本行数：`355`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`TestCreateUser_CreatesUserPreferences, TestCreateUser_RollbackOnPreferencesError, TestCreateUser_InvalidPermissions, TestCreateUser_MultipleUsers, TestCreateUser_InvalidJSON, TestCreateUser_DuplicateEmail`
- 直接依赖：`backend/pkg/server/auth`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/server/services/vecstorelogs.go`

- 文件类型：`.go`
- 大小：`7390` 字节
- 文本行数：`223`
- 所属分组：`backend/pkg/server`
- 所属包/模块：`services`
- 推断作用：REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。
- 生成文件：`否`
- 关键导出/符号：`VecstorelogService, NewVecstorelogService, GetVecstorelogs, GetFlowVecstorelogs`
- 直接依赖：`backend/pkg/server/logger`, `backend/pkg/server/models`, `backend/pkg/server/rdb`, `backend/pkg/server/response`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/router.go`
