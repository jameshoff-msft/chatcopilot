// Copyright (c) Microsoft. All rights reserved.

using System.ComponentModel.DataAnnotations;

namespace CopilotChat.WebApi.Options;

/// <summary>
/// Configuration settings for connecting to Azure Cognitive Search.
/// </summary>
public sealed class AzureCognitiveSearchOptions
{
    public const string PropertyName = "AzureCognitiveSearch";
    /// <summary>
    /// Gets or sets the endpoint protocol and host (e.g. https://contoso.search.windows.net).
    /// </summary>
    [Required, Url]
    public string Endpoint { get; set; } = string.Empty;

    /// <summary>
    /// Key to access Azure Cognitive Search.
    /// </summary>
    [Required, NotEmptyOrWhitespace]
    public string Key { get; set; } = string.Empty;

    /// <summary>
    /// Prebuilt Index to use if not null.
    /// </summary>
    [NotEmptyOrWhitespace]
    public string Index { get; set; } = string.Empty;
}
