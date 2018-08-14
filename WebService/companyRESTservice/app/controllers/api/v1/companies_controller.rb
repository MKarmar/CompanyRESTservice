module Api
  module V1
    class CompaniesController < ApplicationController
      def index
        companies = Company.order('created_at DESC')
        render json: {status: 'Success', message: 'Loaded companies', data: companies}, status: :ok
      end

      def show
        companies = Company.find(params[:id])
        render json: {status: 'Success', message: 'Loaded companies', data: companies}, status: :ok
      end

      def create
        companies = Company.new(companies_params)
        if companies.save
          render json: {status: 'Success', message: 'Loaded companies', data: companies}, status: :ok
        else
          render json: {status: 'Error', message: 'Company not saved', data: companies.errors}, status: :unprocessable_entity
        end
      end

      def destroy
        companies = Company.find(params[:id])
        companies.destroy
        render json: {status: 'Success', message: 'Deleted companies', data: companies}, status: :ok
      end

      def update
        companies = Company.find(params[:id])
        if companies.update_attributes(companies_params)
          render json: {status: 'Success', message: 'Updated company', data: companies}, status: :ok
        else
          render json: {status: 'Error', message: 'Company not updated', data: companies.errors}, status: :unprocessable_entity
        end
      end

      private
      def companies_params
        params.permit(:Name, :Address, :City, :Country, :E_Mail, :Phone_number, :Beneficial_owner)
      end
    end
  end
end
