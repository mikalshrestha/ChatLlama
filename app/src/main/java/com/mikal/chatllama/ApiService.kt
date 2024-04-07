package com.mikal.chatllama

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

/**
 * Created by Mikal Shrestha on 03/04/2024.
 */
interface ApiService {

    @POST("llm/generate_text")
    fun createPost(@Body post: ChatModelRequest): Call<ChatModelResponse>
}